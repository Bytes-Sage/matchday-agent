# MatchDay Agent

MatchDay Agent is a World Cup 2026 match-day planning AI agent backend built for the Google Cloud Rapid Agent Hackathon.

## Tech Stack

- **Language:** Python 3.11+
- **Agent Framework:** Google Agent Development Kit (ADK) (`google-adk`)
- **LLM:** Gemini 2.5 Flash
- **MCP Server:** MongoDB MCP Server (`mongodb-mcp-server`)
- **API Framework:** FastAPI
- **Database:** MongoDB
- **Deployment:** Google Cloud Run (Dockerized)

## Architecture

```text
[ Next.js Frontend ]
        │
    (REST API)
        ▼
[ FastAPI Server ] ──► [ MatchDay Agent (ADK) ] ──► [ Gemini 2.5 Flash ]
                              │
                      (MCP Protocol via stdio)
                              ▼
                  [ MongoDB MCP Server (npx) ]
                              │
                      (MongoDB Query)
                              ▼
                   [ MongoDB Atlas Cluster ]
                 (matches, venues, cities, etc.)
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd matchday-agent
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Copy `.env.example` to `.env` and fill in your MongoDB URI and GCP project details:
   ```bash
   cp .env.example .env
   ```
   *Note: Ensure you have a MongoDB cluster running and have the connection string.*

4. **Install Node.js (for MongoDB MCP Server):**
   Ensure you have Node.js 20+ installed to run the MongoDB MCP server via `npx`.

5. **Seed the Database:**
   Populate your MongoDB database with the required World Cup 2026 data:
   ```bash
   python -m data.seed
   ```

6. **Run the API Server:**
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## API Documentation

The server exposes a REST API for the frontend:

- `GET /api/health` - Check if the API and Agent are healthy.
- `POST /api/chat` - Send a message to the agent.
  - Request body: `{"message": "Plan my day in New York", "session_id": "optional-id"}`
- `GET /api/sessions/{session_id}` - Retrieve the chat history for a session.
- `DELETE /api/sessions/{session_id}` - Delete a session.

## Docker Deployment (Google Cloud Run)

You can build and run the Docker image locally or deploy it to Google Cloud Run.

```bash
docker build -t matchday-agent .
docker run -p 8000:8000 --env-file .env matchday-agent
```

## License

MIT License. See [LICENSE](LICENSE) for more information.
