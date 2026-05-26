Build the complete backend for "MatchDay Agent" — a World Cup 2026 match-day planning AI agent. This is for the Google Cloud Rapid Agent Hackathon. Follow every specification exactly.

## Tech Stack (MANDATORY — do not change)

- **Language:** Python 3.11+
- **Agent Framework:** Google Agent Development Kit (ADK) — `google-adk`
- **LLM:** Gemini 2.5 Flash (via ADK)
- **MCP Server:** MongoDB MCP Server (`mongodb-mcp-server` npm package)
- **API Framework:** FastAPI (to expose the agent as a REST API for the Next.js frontend)
- **Deployment Target:** Google Cloud Run (Dockerfile required)

## Project Structure

Create this exact structure:

```
matchday-agent/
├── agent/
│   ├── __init__.py
│   ├── agent.py              # Main ADK agent definition
│   ├── prompt.py             # System prompt for the agent
│   └── tools.py              # Any custom tools (if needed beyond MCP)
├── api/
│   ├── __init__.py
│   ├── main.py               # FastAPI app entry point
│   ├── routes.py             # API endpoints
│   ├── models.py             # Pydantic request/response models
│   └── middleware.py         # CORS middleware
├── data/
│   └── seed.py               # MongoDB seed script (all World Cup data)
├── config/
│   ├── __init__.py
│   └── settings.py           # Environment variables and config
├── tests/
│   ├── __init__.py
│   ├── test_agent.py         # Agent integration tests
│   └── test_api.py           # API endpoint tests
├── .env.example              # Template for environment variables
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── LICENSE                   # MIT License (MANDATORY for hackathon)
├── README.md
└── pyproject.toml
```

## 1. Configuration — `config/settings.py`

Use pydantic-settings to load environment variables:

```python
# Required env vars:
MONGODB_URI          # MongoDB Atlas connection string (e.g., mongodb+srv://...)
MONGODB_DATABASE     # "worldcup2026"
GOOGLE_CLOUD_PROJECT # GCP project ID
GOOGLE_CLOUD_LOCATION # "us-central1"
GEMINI_MODEL         # "gemini-2.5-flash"
HOST                 # "0.0.0.0"
PORT                 # 8000
CORS_ORIGINS         # Comma-separated frontend URLs
```

## 2. Agent Definition — `agent/agent.py`

Use the Google ADK to create the agent with MongoDB MCP Server as the tool source:

```python
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset, StdioServerParameters

# The MongoDB MCP Server runs as a subprocess via npx
# ADK's McpToolset handles the stdio MCP protocol automatically

mongodb_mcp_params = StdioServerParameters(
    command="npx",
    args=["-y", "mongodb-mcp-server@latest"],
    env={
        "MDB_MCP_CONNECTION_STRING": settings.MONGODB_URI,
        "MDB_MCP_READ_ONLY": "true",
        "MDB_MCP_LOG_LEVEL": "info"
    }
)

agent = Agent(
    name="matchday_agent",
    model=settings.GEMINI_MODEL,
    description="A World Cup 2026 match-day planning assistant",
    instruction=SYSTEM_PROMPT,  # From prompt.py
    tools=[McpToolset(server_params=mongodb_mcp_params)]
)
```

**IMPORTANT:** Check the actual Google ADK documentation for the correct import paths and API. The above is the intended pattern — adapt the exact class names and parameters to match the current ADK version. Install with `pip install google-adk`.

## 3. System Prompt — `agent/prompt.py`

This is the instruction that tells the agent how to behave. Store it as a constant:

```
SYSTEM_PROMPT = """
You are MatchDay Agent — an expert FIFA World Cup 2026 match-day planning assistant.

## Your Database
You have access to a MongoDB database called "worldcup2026" with these collections:
- **matches**: All 64 World Cup matches (group stage + knockout) with teams, dates, venues, cities, and description embeddings
- **venues**: 16 official World Cup stadiums with capacity, location coordinates, parking, transit info, and accessibility details
- **cities**: 16 host city guides with safety info, weather, local tips, emergency contacts, and cultural notes
- **restaurants**: ~200 restaurants near World Cup venues with cuisine, price range, ratings, location coordinates, and match-day hours
- **fan_zones**: Official FIFA Fan Festival locations with coordinates, capacity, and schedule
- **transport**: Transit guides for each host city with subway, bus, ride-share, and parking information

## Your Capabilities

### 1. Match Finder
When users ask about matches, query the `matches` collection using:
- `find` with filters on `city`, `date`, `homeTeam`, `awayTeam`, `stage`, `group`
- For semantic queries like "exciting match" or "big atmosphere", use vector search on the `embedding` field
- Always return: teams, date/time, venue name, city, and stage

### 2. Match Day Planner
When users ask to plan their day, chain multiple queries:
1. Find the match details from `matches`
2. Get venue info from `venues` (parking, gate times, transit)
3. Find nearby restaurants from `restaurants` using geospatial `$near` query on venue coordinates
4. Get fan zone info from `fan_zones` for that city
5. Get transport info from `transport` for that city
6. Synthesize into a structured timeline:
   - Morning: Travel tips + what to pack
   - Pre-match (3-4 hours before): Restaurant recommendation + fan zone visit
   - Match time: Gate info, seat info, prohibited items
   - Post-match: Safe transport home, late-night food options

### 3. City Intelligence
When users ask about a host city or venue:
- Query `cities` for safety guides, weather, tips, emergency contacts
- Query `venues` for stadium-specific info
- Query `transport` for getting around
- Present as a travel-guide-style briefing

## Response Format
- Be conversational but informative
- Use bullet points for lists
- Include specific details (times, prices, distances)
- When showing matches, format as: "🏟️ [HomeTeam] vs [AwayTeam] — [Date] at [Venue], [City]"
- When showing a day plan, use a timeline format with times
- Always cite which city/venue the information is about
- If you're unsure about data, say so — don't make up information

## Rules
- Only use data from the MongoDB database — do not hallucinate match schedules or venue details
- All 2026 World Cup matches are in USA, Canada, and Mexico
- Dates are in UTC — mention the local timezone when relevant
- Prices are in USD for US venues, CAD for Canadian venues, MXN for Mexican venues
"""
```

## 4. FastAPI Server — `api/main.py`

Create a FastAPI app that exposes the agent:

### Endpoints:

```
POST /api/chat
  Request:  { "message": "string", "session_id": "string" (optional) }
  Response: { "response": "string", "session_id": "string", "tool_calls": [...] }

GET /api/health
  Response: { "status": "healthy", "agent": "matchday_agent", "version": "1.0.0" }

GET /api/sessions/{session_id}
  Response: { "session_id": "string", "messages": [...] }

DELETE /api/sessions/{session_id}
  Response: { "status": "deleted" }
```

### Chat endpoint implementation:
- Create an ADK Runner with the agent
- Maintain session state using ADK's InMemorySessionService (or a simple dict for hackathon)
- On POST /api/chat:
  1. Get or create a session for the session_id
  2. Send the user message to the agent via runner.run_async()
  3. Collect the agent's response (including any tool calls it made)
  4. Return the response text and metadata

### CORS:
- Allow origins from CORS_ORIGINS env var
- Allow all methods and headers (hackathon — not production)

## 5. Pydantic Models — `api/models.py`

```python
class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None

class ToolCall(BaseModel):
    tool_name: str
    arguments: dict
    result: str | None = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    tool_calls: list[ToolCall] = []
    timestamp: str

class HealthResponse(BaseModel):
    status: str
    agent: str
    version: str
```

## 6. Seed Script — `data/seed.py`

Create a Python script that populates all 6 collections in the `worldcup2026` database.

### matches collection (create at least 20 matches covering all 16 venues):

Include these real 2026 World Cup details:
- **Host cities (USA):** New York/NJ (MetLife), Los Angeles (SoFi), Dallas (AT&T), Houston (NRG), Atlanta (Mercedes-Benz), Philadelphia (Lincoln Financial), Seattle (Lumen), Miami (Hard Rock), Boston (Gillette), Kansas City (Arrowhead), San Francisco (Levi's)
- **Host cities (Mexico):** Mexico City (Estadio Azteca), Guadalajara (Estadio Akron), Monterrey (Estadio BBVA)
- **Host cities (Canada):** Toronto (BMO Field), Vancouver (BC Place)
- **Match format:** 48 teams, 12 groups of 4, then knockout rounds
- **Dates:** June 11 — July 19, 2026
- Each match document must have:
  - `_id`, `matchNumber`, `stage`, `group`, `homeTeam`, `awayTeam`
  - `date` (ISO 8601), `venueId`, `city`, `country`
  - `description` (a rich 1-2 sentence description of the match for vector search)
  - `embedding` field — leave as an empty array `[]` (we'll generate embeddings later with Voyage AI or Gemini)

### venues collection (all 16 stadiums):

Each venue must have:
- `_id` (slug like "metlife"), `name`, `city`, `state`/`province`, `country`
- `capacity` (integer)
- `location` with GeoJSON format: `{"type": "Point", "coordinates": [longitude, latitude]}`
  - Use real coordinates from Google Maps
- `gateOpenTime`, `parking` (lots count, cost, open time)
- `transit` (train, bus, ride-share info)
- `prohibitedItems` (array of strings)
- `accessibility` (ADA/accessibility info)
- `weather` (typical June/July weather)

### cities collection (all 16 host cities):

Each city must have:
- `_id` (slug like "new-york"), `name`, `state`/`province`, `country`
- `timezone` (e.g., "America/New_York")
- `safety` (general safety tips, areas to avoid, emergency numbers)
- `weather` (typical June/July conditions)
- `localTips` (array of 3-5 insider tips)
- `emergencyContacts` (police, ambulance, embassy numbers)
- `currency`, `language`
- `fanExperience` (what makes this city special for fans)

### restaurants collection (at least 3 per venue = ~48 restaurants):

Each restaurant must have:
- `_id`, `name`, `cuisine`, `priceRange` ("$" to "$$$$")
- `rating` (float, 3.5-5.0)
- `venueId` (which stadium it's near)
- `location` with GeoJSON: `{"type": "Point", "coordinates": [lng, lat]}`
  - Use realistic coordinates near the actual venue
- `distanceFromVenue`, `reservationRequired` (boolean)
- `matchDayHours`, `fanFriendly` (boolean)
- `description` (one sentence about the restaurant)

### fan_zones collection (at least 1 per city = ~16):

Each fan zone must have:
- `_id`, `name`, `city`, `country`
- `location` with GeoJSON
- `capacity` (integer)
- `schedule` (daily opening/closing times)
- `amenities` (array: screens, food, drinks, merchandise, etc.)
- `freeEntry` (boolean)

### transport collection (1 per city = 16):

Each transport guide must have:
- `_id`, `city`, `country`
- `airport` (name, code, distance to city center)
- `publicTransit` (subway/bus/tram details)
- `rideshare` (Uber/Lyft availability, estimated costs)
- `parking` (general city parking info)
- `matchDayShuttles` (if available)
- `tips` (array of 3-5 transport tips)

### Seed script requirements:
- Use `pymongo` to connect and insert
- Drop existing collections before seeding (idempotent)
- Print progress as it seeds each collection
- Run with: `python -m data.seed`

## 7. Dockerfile

```dockerfile
FROM python:3.11-slim

# Install Node.js (needed for MongoDB MCP Server via npx)
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 8. requirements.txt

```
google-adk>=0.3.0
google-cloud-aiplatform>=1.60.0
fastapi>=0.111.0
uvicorn[standard]>=0.30.0
pydantic>=2.0
pydantic-settings>=2.0
pymongo>=4.7.0
python-dotenv>=1.0.0
httpx>=0.27.0
```

**NOTE:** Check the latest version of `google-adk` on PyPI and use that. If `google-adk` is not available, use `google-genai` with the Agent class instead.

## 9. .env.example

```env
MONGODB_URI=mongodb+srv://matchday_admin:YOUR_PASSWORD@matchdaycluster.xxxxx.mongodb.net/worldcup2026?retryWrites=true&w=majority
MONGODB_DATABASE=worldcup2026
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GEMINI_MODEL=gemini-2.5-flash
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

## 10. .gitignore

```
__pycache__/
*.pyc
.env
.venv/
venv/
*.egg-info/
dist/
build/
.pytest_cache/
node_modules/
```

## 11. LICENSE

Use MIT License with the current year (2026) and copyright holder name as the hackathon participant.

## 12. README.md

Write a clear README with:
- Project name and one-line description
- "Built for the Google Cloud Rapid Agent Hackathon"
- Tech stack section
- Setup instructions (clone, install, env vars, seed, run)
- API documentation
- Architecture diagram (text-based)
- Screenshots placeholder
- License (MIT)

## Critical Requirements

1. **The agent MUST use MongoDB MCP Server as the tool source** — not direct pymongo calls in the agent. The MCP server is what the hackathon judges are evaluating.
2. **The seed script uses pymongo directly** — that's fine, it's a one-time setup script, not the agent.
3. **The agent must demonstrate multi-step tool calling** — a single query asking to "plan my day" should result in 3-5 sequential MCP tool calls (find match → find venue → find restaurants → find transport).
4. **All data must be realistic** — use real stadium names, real coordinates, real capacity numbers. Don't make up fictional venues.
5. **Include error handling** — the agent should gracefully handle when no matches are found, when a city isn't a host city, etc.
6. **Include logging** — use Python's logging module, log all tool calls and agent decisions.
