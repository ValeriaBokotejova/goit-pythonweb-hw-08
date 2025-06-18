# goit-pythonweb-hw-08

# 📇 Contacts API

A RESTful API for managing personal contacts built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.
Supports full CRUD operations and filtering features.

---

## 🚀 Features

- 📥 Create a new contact
- 📄 Get all contacts
- 🔍 Get contact by ID
- 📝 Update contact
- ❌ Delete contact
- 🔎 Search contacts by first name, last name, or email
- 🎉 Get contacts with upcoming birthdays in the next 7 days

---

## 🛠️ Tech Stack

- ⚡ FastAPI
- 🐘 PostgreSQL
- 🧬 SQLAlchemy (async)
- 📦 Alembic (migrations)
- 🧪 Pydantic
- 🐍 Python 3.12+

---


## 🔧 Setup & Run

1. **Clone the repo**
    ```bash
    git clone https://github.com/ValeriaBokotejova/goit-pythonweb-hw-08.git
    cd contacts-api
    ```
2. **Create virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # or `venv\Scripts\activate` on Windows
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure environment**
Create a .env file and fill in your PostgreSQL settings:
    ```ini
    POSTGRES_DB=contacts_db
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432

    DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/contacts_db
    ```
5. **Run migrations**
    ```bash
    alembic upgrade head
    ```
6. **Run the app**
    ```bash
    uvicorn app.main:app --reload
    ```
7. **Open in browser**
    - Swagger UI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc

---

## 📬 API Endpoints

| Method | Endpoint                           | Description                 |
|--------|------------------------------------|-----------------------------|
| POST   | `/api/contacts/`                   | Create a new contact        |
| GET    | `/api/contacts/`                   | Get all contacts or filter  |
| GET    | `/api/contacts/{id}`               | Get contact by ID           |
| PUT    | `/api/contacts/{id}`               | Update contact              |
| DELETE | `/api/contacts/{id}`               | Delete contact              |
| GET    | `/api/contacts/upcoming/birthdays` | Birthdays in next 7 days 🎂 |
