from app.evaluators.base import Evaluator

class LocalLLMJudge(Evaluator):
    name = "local_llm"

    async def evaluate(self, conversation):
        return {
            "helpfulness": 0.7,
            "correctness": 0.75,
            "clarity": 0.7,
            "overall": 0.72
        }
