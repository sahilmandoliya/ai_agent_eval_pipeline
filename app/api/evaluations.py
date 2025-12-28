from fastapi import APIRouter
from app.services.evaluation_service import run_evaluation
from app.core.database import SessionLocal
from app.models.orm import EvaluationORM

router = APIRouter()

@router.post("/run/{conversation_id}")
async def evaluate(conversation_id: str):
    return await run_evaluation(conversation_id)

@router.get("/{evaluation_id}")
async def get_evaluation(evaluation_id: str):
    async with SessionLocal() as session:
        eval_obj = await session.get(EvaluationORM, evaluation_id)
        if not eval_obj:
            return {"error": "Not found"}

        return {
            "evaluation_id": eval_obj.evaluation_id,
            "conversation_id": eval_obj.conversation_id,
            "scores": eval_obj.scores,
            "suggestions": eval_obj.suggestions,
            "disagreement": eval_obj.disagreement
        }
