from fastapi import FastAPI
from app.routers import contacts

app = FastAPI(
    title="Contacts API",
    description="A RESTful API for managing contacts using FastAPI and PostgreSQL.",
    version="1.0.0",
)

# Include contacts router
app.include_router(contacts.router, prefix="/api/contacts", tags=["Contacts"])
