from fastapi import APIRouter, HTTPException
from app.models.schemas import ConversationCreate
from app.services.ingest_service import ingest_conversation

router = APIRouter()

@router.post("/")
async def ingest(conv: ConversationCreate):
    return await ingest_conversation(conv)
