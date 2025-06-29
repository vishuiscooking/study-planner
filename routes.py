# backend/routes.py

from fastapi import APIRouter, HTTPException
from typing import List
from models import Note, NoteCreate
import db

note_routes = APIRouter()

# Initialize DB once when app starts
db.init_db()

@note_routes.get("/notes", response_model=List[Note])
def read_notes():
    return db.get_all_notes()

@note_routes.get("/notes/{note_id}", response_model=Note)
def read_note(note_id: int):
    note = db.get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@note_routes.post("/notes", response_model=Note)
def create_note(note: NoteCreate):
    return db.create_note(note)

@note_routes.put("/notes/{note_id}", response_model=Note)
def update_existing_note(note_id: int, note: NoteCreate):
    existing = db.get_note(note_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db.update_note(note_id, note)

@note_routes.delete("/notes/{note_id}")
def delete_existing_note(note_id: int):
    existing = db.get_note(note_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete_note(note_id)
    return {"message": "Note deleted successfully"}

