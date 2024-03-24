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

def save_notes(notes):
    try:
        with open(NOTES_FILE, 'w') as file:
            json.dump(notes, file, indent=4)
    except Exception as e:
        print("An error occurred while saving notes:", e)
        
def read_notes():
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return
        with open(NOTES_FILE) as file:
            notes = json.load(file)
            for note in notes:
                print("ID: ", note["id"])
                print("Title: ", note["title"])
                print("Body: ", note["body"])
                print("Created on: ", note["created_date"])
                print()
    except Exception as e:
        print("An error occurred while reading notes:", e)
