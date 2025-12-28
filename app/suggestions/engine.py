def generate_suggestions(scores):
    suggestions = []

    tool_acc = scores.get("tool_accuracy", 1)
    coherence = scores.get("coherence", 1)

    if tool_acc < 1:
        suggestions.append({
            "type": "tool",
            "suggestion": "Tool parameters seem incorrect or missing.",
            "confidence": 0.9
        })

    if coherence < 0.8:
        suggestions.append({
            "type": "coherence",
            "suggestion": "Conversation context may be drifting.",
            "confidence": 0.7
        })

    return suggestions
