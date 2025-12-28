from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api import conversations, evaluations
from app.models.orm import Base
from app.core.database import engine

setup_logging()

app = FastAPI(title="AI Agent Evaluation Pipeline")

app.include_router(conversations.router, prefix="/conversations", tags=["Conversations"])
app.include_router(evaluations.router, prefix="/evaluations", tags=["Evaluations"])

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
