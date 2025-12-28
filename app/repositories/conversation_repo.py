from app.models.orm import ConversationORM

class ConversationRepository:
    @staticmethod
    async def get(session, conversation_id):
        return await session.get(ConversationORM, conversation_id)