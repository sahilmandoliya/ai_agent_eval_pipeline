from app.evaluators.base import Evaluator

class CoherenceEvaluator(Evaluator):
    name = "coherence"

    async def evaluate(self, conversation):
        turns = conversation.get("turns", [])
        if len(turns) < 2:
            return {"coherence": 1.0}

        first_user = next((t["content"] for t in turns if t["role"] == "user"), "")
        last_assistant = next((t["content"] for t in reversed(turns) if t["role"] == "assistant"), "")

        if first_user and last_assistant and first_user not in last_assistant:
            return {"coherence": 0.7}

        return {"coherence": 0.9}
