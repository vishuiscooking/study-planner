# backend/db.py

import sqlite3
from datetime import datetime
from models import NoteCreate, Note

DB_NAME = "notes.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_all_notes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    conn.close()
    return [Note(id=row[0], title=row[1], content=row[2],
                 created_at=row[3], updated_at=row[4]) for row in rows]

def get_note(note_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Note(id=row[0], title=row[1], content=row[2],
                    created_at=row[3], updated_at=row[4])
    return None

def create_note(note: NoteCreate):
    now = datetime.utcnow().isoformat()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content, created_at, updated_at) VALUES (?, ?, ?, ?)",
        (note.title, note.content, now, now)
    )
    conn.commit()
    note_id = cursor.lastrowid
    conn.close()
    return get_note(note_id)

def update_note(note_id: int, note: NoteCreate):
    now = datetime.utcnow().isoformat()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE notes SET title = ?, content = ?, updated_at = ? WHERE id = ?",
        (note.title, note.content, now, note_id)
    )
    conn.commit()
    conn.close()
    return get_note(note_id)

def delete_note(note_id: int):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

