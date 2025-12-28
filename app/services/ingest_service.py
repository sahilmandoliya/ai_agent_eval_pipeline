import logging
from app.core.database import SessionLocal
from app.models.orm import ConversationORM

log = logging.getLogger(__name__)

async def ingest_conversation(conv):
    log.info(f"Ingesting {conv.conversation_id}")

    async with SessionLocal() as session:
        obj = ConversationORM(
            conversation_id=conv.conversation_id,
            agent_version=conv.agent_version,
            data=conv.dict()
        )
        session.add(obj)
        await session.commit()

    log.info(f"Stored conversation {conv.conversation_id}")

    return {"status": "stored", "conversation_id": conv.conversation_id}
