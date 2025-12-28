from uuid import uuid4
from app.core.database import SessionLocal
from app.models.orm import ConversationORM, EvaluationORM
from app.evaluators.mock_llm import MockLLMJudge
from app.evaluators.openai_llm import OpenAILLMJudge
from app.evaluators.local_llm import LocalLLMJudge
from app.evaluators.tool_eval import ToolEvaluator
from app.evaluators.coherence_eval import CoherenceEvaluator
from app.suggestions.engine import generate_suggestions
from app.core.config import settings

async def run_evaluation(conversation_id: str):
    async with SessionLocal() as session:
        conv = await session.get(ConversationORM, conversation_id)
        if not conv:
            return {"error": "Conversation not found"}

        data = conv.data
        feedback = data.get("feedback") or {}
        human_rating = feedback.get("user_rating")


        if settings.USE_OPENAI:
            llm = OpenAILLMJudge()
        elif settings.USE_LOCAL_LLM:
            llm = LocalLLMJudge()
        else:
            llm = MockLLMJudge()

        tool_eval = ToolEvaluator()
        coherence_eval = CoherenceEvaluator()

        llm_scores = await llm.evaluate(data)
        tool_scores = await tool_eval.evaluate(data)
        coherence_scores = await coherence_eval.evaluate(data)

        scores = {**llm_scores, **tool_scores, **coherence_scores}

        if human_rating:
            scores["overall"] = (scores["overall"] + human_rating / 5) / 2

        disagreement = None
        if human_rating:
            disagreement = abs(scores["overall"] - human_rating / 5)

        suggestions = generate_suggestions(scores)

        evaluation_id = str(uuid4())

        session.add(EvaluationORM(
            evaluation_id=evaluation_id,
            conversation_id=conversation_id,
            scores=scores,
            suggestions=suggestions,
            disagreement=disagreement
        ))

        await session.commit()

    return {
        "evaluation_id": evaluation_id,
        "conversation_id": conversation_id,
        "scores": scores,
        "suggestions": suggestions,
        "disagreement": disagreement
    }
