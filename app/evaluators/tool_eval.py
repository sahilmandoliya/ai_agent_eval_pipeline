import re
from app.evaluators.base import Evaluator

class ToolEvaluator(Evaluator):
    name = "tool"

    def _infer_expected_tool(self, user_text: str):
        user_text = user_text.lower()
        if "flight" in user_text or "book" in user_text or "search" in user_text:
            return "flight_search"
        if "refund" in user_text:
            return "process_refund"
        if "weather" in user_text:
            return "get_weather"
        return None

    def _required_args_for(self, tool_name: str):
        if tool_name == "flight_search":
            return ["destination"]
        if tool_name == "process_refund":
            return ["order_id"]
        if tool_name == "get_weather":
            return ["location"]
        return []

    async def evaluate(self, conversation):
        turns = conversation.get("turns", [])

        user_text = " ".join(
            t.get("content", "") for t in turns if t.get("role") == "user"
        )

        expected_tool = self._infer_expected_tool(user_text)

        tool_calls = []
        for t in turns:
            tool_calls.extend(t.get("tool_calls") or [])

        if expected_tool and not tool_calls:
            return {
                "tool_accuracy": 0.0,
                "tool_issue": "expected_tool_not_called"
            }

        for call in tool_calls:
            tool_name = call.get("tool_name")
            params = call.get("parameters", {}) or {}

            if expected_tool and tool_name != expected_tool:
                return {
                    "tool_accuracy": 0.0,
                    "tool_issue": "unexpected_tool_called"
                }

            required = self._required_args_for(tool_name)
            for arg in required:
                if arg not in params:
                    return {
                        "tool_accuracy": 0.0,
                        "tool_issue": "missing_required_argument"
                    }

        return {"tool_accuracy": 1.0}
