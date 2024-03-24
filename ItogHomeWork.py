import json
import datetime
import os

NOTES_FILE = 'notes.json'

def create_note():
    try:
        note_id = input("Enter note ID: ")
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        note = {
            "id": note_id,
            "title": title,
            "body": body,
            "created_date": created_date
        }
        return note
    except Exception as e:
        print("An error occurred while creating the note:", e)
        return None

    return note
