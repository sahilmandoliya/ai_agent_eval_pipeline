# AI Agent Evaluation Pipeline

This project provides a backend service to ingest AI agent conversations and evaluate them across multiple quality dimensions such as correctness, clarity, tool usage, and coherence.  
The goal is to make agent behavior observable, debuggable, and measurable in a structured way.

Live demo:  
https://ai-agent-eval-pipeline.onrender.com/docs

---

## Overview

The system accepts conversation logs, runs multiple evaluators over them, aggregates the results, and produces a structured evaluation report along with actionable suggestions.

It is designed to be:
- Modular (new evaluators can be added easily)
- Deterministic where possible, probabilistic where needed
- Explainable (scores are accompanied by reasoning)
- Production-oriented (clear APIs, persistence, observability)

---

## High-Level Architecture

```
Client / Agent Logs
        ↓
     API Layer (FastAPI)
        ↓
     Persistence Layer
        ↓
     Evaluation Engine
        ├─ LLM-based evaluator
        ├─ Tool usage evaluator
        ├─ Coherence evaluator
        ↓
     Aggregation + Calibration
        ↓
     Final Evaluation Output
```

---

## Core Components

### Ingestion

Stores structured conversations including:
- Turns (user / assistant / tool)
- Tool calls and parameters
- Metadata and optional feedback

### Evaluators

| Evaluator | Responsibility |
|----------|----------------|
| LLM Judge | Semantic quality (helpfulness, clarity, correctness) |
| Tool Evaluator | Tool usage correctness and schema adherence |
| Coherence Evaluator | Logical and conversational consistency |

### Aggregation

Scores are normalized and combined into an overall score.  
Human feedback (if present) is used to calibrate automated judgments.

---

## API

- `POST /conversations/` — Ingest conversation
- `POST /evaluations/run/{conversation_id}` — Run evaluation
- `GET /evaluations/{evaluation_id}` — Fetch evaluation

Swagger UI is available at `/docs`.

---

## Example Scenarios

### Regression detection

If a tool call changes from:

```json
"parameters": { "destination": "NYC" }
```

to:

```json
"parameters": { "dest": "NYC" }
```

the tool evaluator flags it and reduces tool accuracy.

### Disagreement detection

If the automated score is high but user feedback is very low, the system surfaces disagreement for review.

---

## Configuration

| Variable | Description |
|----------|-------------|
| OPENAI_API_KEY | Enables LLM-based evaluation |
| USE_OPENAI | Toggle LLM usage |
| DATABASE_URL | Override persistence layer |
| LOG_LEVEL | Logging verbosity |

---

## Running locally

```bash
docker build -t ai-eval .
docker run -p 8000:8000 ai-eval
```

Then open http://localhost:8000/docs.

---

## Design Notes

- Deterministic evaluators are preferred where possible (tool usage, coherence).
- LLMs are used only where semantic judgment is required.
- All outputs are structured and inspectable.
- The system favors debuggability over black-box scoring.

---

## Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite (pluggable)
- Docker
- Render

---

## Possible Extensions

- Longitudinal regression tracking
- Golden dataset comparison
- Alerting on score degradation
- Prompt evolution tracking
- Multi-agent analysis
