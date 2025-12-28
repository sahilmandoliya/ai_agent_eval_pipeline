from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import logging

log = logging.getLogger(__name__)
log.info(f"Using database at: {settings.DB_PATH}")

engine = create_async_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
