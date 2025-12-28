from app.evaluators.base import Evaluator

class MockLLMJudge(Evaluator):
    name = "mock_llm"

    async def evaluate(self, conversation):
        return {
            "helpfulness": 0.8,
            "correctness": 0.85,
            "clarity": 0.75,
            "overall": 0.8
        }
