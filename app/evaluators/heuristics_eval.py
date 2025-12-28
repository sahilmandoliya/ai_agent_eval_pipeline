from app.evaluators.base import Evaluator

class HeuristicsEvaluator(Evaluator):
    name = "heuristics"

    async def evaluate(self, conversation):
        turns = conversation.get("turns", [])
        issues = []
        score = 1.0

        for t in turns:
            if not t.get("content") and not t.get("tool_calls"):
                issues.append("Empty message detected")
                score -= 0.2

        return {"heuristics": max(score, 0.0), "issues": issues}
