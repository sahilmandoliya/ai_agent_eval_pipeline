from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, JSON, Float

Base = declarative_base()

class ConversationORM(Base):
    __tablename__ = "conversations"

    conversation_id = Column(String, primary_key=True)
    agent_version = Column(String)
    data = Column(JSON)

class EvaluationORM(Base):
    __tablename__ = "evaluations"

    evaluation_id = Column(String, primary_key=True)
    conversation_id = Column(String, index=True)
    scores = Column(JSON)
    suggestions = Column(JSON)
    disagreement = Column(Float)
