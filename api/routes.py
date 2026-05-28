import uuid
import datetime
import logging
from fastapi import APIRouter, HTTPException
from api.models import ChatRequest, ChatResponse, HealthResponse, ToolCall
from agent.agent import get_runner

logger = logging.getLogger(__name__)

# session memory state
sessions = {}

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        agent="matchday_agent",
        version="1.0.0"
    )

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    session_id = request.session_id or str(uuid.uuid4())
    
    # Very simple dict-based session handling for hackathon
    if session_id not in sessions:
        sessions[session_id] = []
        
    try:
        runner = get_runner()
        logger.info(f"Running agent for session: {session_id}")
        
        from google.genai import types
        
        # Run agent
        result_text = ""
        extracted_tools = []
        
        async for event in runner.run_async(
            user_id="default_user",
            session_id=session_id,
            new_message=types.Content(role="user", parts=[types.Part.from_text(text=request.message)])
        ):
            if hasattr(event, "content") and getattr(event, "content") is not None:
                for part in getattr(event.content, "parts", []):
                    if hasattr(part, "text") and getattr(part, "text"):
                        result_text += part.text
                    if hasattr(part, "function_call") and getattr(part, "function_call"):
                        fc = part.function_call
                        extracted_tools.append(ToolCall(
                            tool_name=getattr(fc, "name", "unknown"),
                            arguments=getattr(fc, "args", {}),
                            result=None
                        ))
        
        # Save message in our hacky dict just to return for GET /sessions/{session_id}
        sessions[session_id].append({"role": "user", "content": request.message})
        sessions[session_id].append({"role": "agent", "content": result_text})
        
        return ChatResponse(
            response=result_text,
            session_id=session_id,
            tool_calls=extracted_tools,
            timestamp=datetime.datetime.utcnow().isoformat()
        )
    except Exception as e:
        logger.error(f"Error during chat: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sessions/{session_id}")
async def get_session(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    return {
        "session_id": session_id,
        "messages": sessions[session_id]
    }

@router.delete("/sessions/{session_id}")
async def delete_session(session_id: str):
    if session_id in sessions:
        del sessions[session_id]
        return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="Session not found")
