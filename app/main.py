from fastapi import FastAPI
from app.routers import contacts
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="Contacts API",
    description="A RESTful API for managing contacts using FastAPI and PostgreSQL.",
    version="1.0.0",
)

# Include contacts router with a specific prefix and tag for grouping in Swagger
app.include_router(contacts.router, prefix="/api/contacts", tags=["Contacts"])
