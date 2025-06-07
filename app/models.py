from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    phone_number = Column(String(20), nullable=False)
    birth_date = Column(Date, nullable=True)
    extra_info = Column(String(250), nullable=True)
