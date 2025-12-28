from pydantic import BaseModel
from typing import List, Optional, Dict

class ToolCall(BaseModel):
    tool_name: str
    parameters: Dict
    result: Optional[Dict]
    latency_ms : Optional[int]

class Turn(BaseModel):
    turn_id: int
    role: str
    content : str
    timestamp : str
    tool_calls: Optional[List[ToolCall]] = []

class Feedback(BaseModel):
    user_rating: Optional[int] = None
    ops_review: Optional[Dict] = None
    annotations: Optional[List[Dict]] = None

class Metadata(BaseModel):
    total_latency_ms: Optional[int] = None
    tool_latency_ms: Optional[int] = None
    mission_completed: Optional[bool] = None


class ConversationCreate(BaseModel):
    conversation_id: str
    agent_version: str
    turns: List[Turn]
    feedback: Optional[Feedback] = None
    metadata: Optional[Metadata] = None
