from app.evaluators.base import Evaluator

class ToolEvaluator(Evaluator):
    name = "tool"

    async def evaluate(self, conversation):
        turns = conversation.get("turns", [])
        for t in turns:
            for call in t.get("tool_calls", []) or []:
                params = call.get("parameters", {})
                if call.get("tool_name") == "flight_search":
                    if "destination" not in params:
                        return {"tool_accuracy": 0.0}
        return {"tool_accuracy": 1.0}
