import os
from app.evaluators.base import Evaluator

class OpenAILLMJudge(Evaluator):
    name = "openai_llm"

    def __init__(self):
        from openai import OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY not set but USE_OPENAI=true")

        self.client = OpenAI(api_key=api_key)

    async def evaluate(self, conversation):
        prompt = f"""
Evaluate the assistant response.
Return JSON: helpfulness, correctness, clarity, overall.
Conversation: {conversation}
"""
        resp = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        import json
        return json.loads(resp.choices[0].message.content)
