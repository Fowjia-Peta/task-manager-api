# Task Manager API

A simple REST API built with FastAPI to manage tasks (CRUD operations).

## Features
- Add a task (POST /tasks)
- View all tasks (GET /tasks)
- Update a task (PUT /tasks/{index})
- Delete a task (DELETE /tasks/{index})

## Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn

## How to Run
1. Install dependencies: pip install fastapi uvicorn
2. Start the server: uvicorn main:app --reload
3. Open the docs: http://127.0.0.1:8000/docs

## Task Format
{
  "title": "Learn FastAPI",
  "done": false
}
