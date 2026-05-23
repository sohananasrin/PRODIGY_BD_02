# PRODIGY_BD_02

Database Integration Task for Backend Development Internship at Prodigy InfoTech.

## Features

- FastAPI backend
- SQLite database integration
- SQLAlchemy ORM
- CRUD Operations
  - Create User
  - Get All Users
  - Get User By ID
  - Update User
  - Delete User
- Environment configuration using .env

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

## Installation

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run server:

```bash
python -m uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

POST /users

GET /users

GET /users/{user_id}

PUT /users/{user_id}

DELETE /users/{user_id}

## Internship Task

Prodigy InfoTech Backend Development Internship - Task 2