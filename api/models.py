from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ToolCall(BaseModel):
    tool_name: str
    arguments: dict
    result: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    tool_calls: List[ToolCall] = []
    timestamp: str

class HealthResponse(BaseModel):
    status: str
    agent: str
    version: str
