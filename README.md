# 🧠 AI Agent Evaluation Pipeline

A modular, extensible backend system for ingesting AI agent conversations and automatically evaluating them using a combination of deterministic rules and LLM-based judgments.

This service supports:
- Conversation ingestion
- Multi-metric evaluation (helpfulness, correctness, clarity, coherence, tool accuracy)
- Human feedback calibration
- Regression detection and disagreement analysis
- Explainable scoring and improvement suggestions

🔗 **Live Demo:**  
https://ai-agent-eval-pipeline.onrender.com/docs

---

## 🚀 Architecture Overview

Client / Agent Logs
    ↓
FastAPI API Layer
    ↓
Persistence (SQLite / ORM)
    ↓
Evaluation Service
    ├── LLM Judge
    ├── Tool Evaluator
    ├── Coherence Evaluator
    ↓
Suggestion Engine
    ↓
Meta Evaluation & Aggregation
    ↓
Final Report


### Flow

1. Client sends a conversation log.
2. The system persists the data.
3. Evaluators run independently.
4. Scores are aggregated and calibrated.
5. Suggestions are generated.
6. Disagreement and regression are computed.

---

## 🧩 Core Concepts

### Conversation Ingestion
Stores structured conversations including turns, tool calls, metadata, and feedback.

### Evaluators

| Evaluator | Purpose |
|----------|----------|
| LLM Judge | Scores semantic quality (helpfulness, correctness, clarity) |
| Tool Evaluator | Verifies correct tool usage and parameter integrity |
| Coherence Evaluator | Ensures conversational flow and logical consistency |

### Hybrid Evaluation

We combine:
- **Deterministic checks** (schema, tool usage, coherence)
- **Probabilistic judgments** (LLM-based scoring)

This improves:
- Reliability
- Explainability
- Debuggability
- Trustworthiness

---

## 🔧 API Endpoints

### 1️⃣ Ingest Conversation

`POST /conversations/`

```json
{
  "conversation_id": "conv_test_1",
  "agent_version": "v1.0",
  "turns": [...],
  "feedback": {...},
  "metadata": {...}
}

2️⃣ Run Evaluation

POST /evaluations/run/{conversation_id}

Returns:

{
  "evaluation_id": "...",
  "scores": {...},
  "suggestions": [...],
  "disagreement": 0.2
}

3️⃣ Get Evaluation

GET /evaluations/{evaluation_id}

🧪 Example Tests
Regression Test

Change tool params:

"parameters": { "dest": "NYC" }


Expected:

tool_accuracy drops

suggestion generated

Disagreement Test

Set:

"user_rating": 1


Expected:

disagreement score increases

⚙️ Configuration

Environment variables:

Variable	Purpose
OPENAI_API_KEY	Enables LLM judging
USE_OPENAI	Toggle OpenAI usage
DATABASE_URL	Override DB
LOG_LEVEL	Logging verbosity
🐳 Running Locally with Docker
docker build -t ai-eval .
docker run -p 8000:8000 ai-eval


Then open:

http://localhost:8000/docs

🧠 Design Principles

Modular evaluator system

Explainable scoring

Deterministic + probabilistic hybrid model

Easy to extend with new evaluators

Production-ready observability

📦 Tech Stack

FastAPI

SQLAlchemy

Pydantic

OpenAI API (optional)

SQLite (pluggable)

Docker

Render

🧭 Future Improvements

Regression trend analysis

Golden dataset comparison

Alerting on metric drift

Prompt evolution tracking

Multi-agent evaluation

