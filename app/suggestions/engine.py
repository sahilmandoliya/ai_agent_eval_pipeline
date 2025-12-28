def generate_suggestions(scores):
    suggestions = []

    tool_acc = scores.get("tool_accuracy", 1)
    tool_issue = scores.get("tool_issue")
    coherence = scores.get("coherence", 1)

    if tool_acc < 1:
        if tool_issue == "expected_tool_not_called":
            suggestions.append({
                "type": "tool",
                "suggestion": "The assistant should call the appropriate tool when user intent implies an action.",
                "confidence": 0.9
            })
        elif tool_issue == "unexpected_tool_called":
            suggestions.append({
                "type": "tool",
                "suggestion": "The assistant called a tool that does not match user intent.",
                "confidence": 0.8
            })
        elif tool_issue == "missing_required_argument":
            suggestions.append({
                "type": "tool",
                "suggestion": "The tool was called but with missing required parameters.",
                "confidence": 0.85
            })
        else:
            suggestions.append({
                "type": "tool",
                "suggestion": "Tool usage may be incorrect.",
                "confidence": 0.7
            })

    if coherence < 0.8:
        suggestions.append({
            "type": "coherence",
            "suggestion": "Conversation context may be drifting or inconsistent.",
            "confidence": 0.7
        })

    return suggestions
