from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app import models, schemas

router = APIRouter()


@router.post("/", response_model=schemas.ContactRead)
async def create_contact(contact: schemas.ContactCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new contact.
    """
    new_contact = models.Contact(**contact.dict())
    db.add(new_contact)
    await db.commit()
    await db.refresh(new_contact)
    return new_contact


@router.get("/", response_model=List[schemas.ContactRead])
async def read_contacts(
    db: AsyncSession = Depends(get_db),
    first_name: Optional[str] = Query(None),
    last_name: Optional[str] = Query(None),
    email: Optional[str] = Query(None)
):
    """
    Get all contacts or filter by first name, last name, or email.
    """
    query = select(models.Contact)

    if first_name:
        query = query.filter(models.Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.filter(models.Contact.last_name.ilike(f"%{last_name}%"))
    if email:
        query = query.filter(models.Contact.email.ilike(f"%{email}%"))

    result = await db.execute(query)
    return result.scalars().all()


@router.get("/{contact_id}", response_model=schemas.ContactRead)
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get a contact by its ID.
    """
    result = await db.execute(select(models.Contact).where(models.Contact.id == contact_id))
    contact = result.scalar_one_or_none()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.put("/{contact_id}", response_model=schemas.ContactRead)
async def update_contact(contact_id: int, updated_data: schemas.ContactUpdate, db: AsyncSession = Depends(get_db)):
    """
    Update an existing contact.
    """
    result = await db.execute(select(models.Contact).where(models.Contact.id == contact_id))
    contact = result.scalar_one_or_none()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(contact, key, value)

    await db.commit()
    await db.refresh(contact)
    return contact


@router.delete("/{contact_id}")
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete a contact by its ID.
    """
    result = await db.execute(select(models.Contact).where(models.Contact.id == contact_id))
    contact = result.scalar_one_or_none()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    await db.delete(contact)
    await db.commit()
    return {"message": "Contact deleted successfully"}


@router.get("/upcoming/birthdays", response_model=List[schemas.ContactRead])
async def upcoming_birthdays(db: AsyncSession = Depends(get_db)):
    """
    Get contacts with birthdays in the next 7 days.
    """
    today = datetime.today().date()
    in_seven_days = today + timedelta(days=7)

    result = await db.execute(select(models.Contact))
    contacts = result.scalars().all()

    upcoming = [
        c for c in contacts
        if c.birth_date and today <= c.birth_date.replace(year=today.year) <= in_seven_days
    ]

    return upcoming
