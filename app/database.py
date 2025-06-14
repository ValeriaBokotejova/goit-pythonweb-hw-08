from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import declarative_base
from app.config import settings

# Declarative base for models
Base = declarative_base()

# Create async engine
engine: AsyncEngine = create_async_engine(settings.database_url, echo=True)

# Session factory
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


# Dependency
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
