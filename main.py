import json
import csv
import datetime
import os

NOTES_FILE = "notes.json"


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            try:
                notes = json.load(file)
            except json.JSONDecodeError:
                notes = []
    else:
        notes = []
    return notes


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)


def add_note(title, body):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": str(datetime.datetime.now()),
    }
    notes.append(note)
    save_notes(notes)
    print("Note saved successfully")


def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")
    print("\n")


def edit_note(note_id, title, body):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["timestamp"] = str(datetime.datetime.now())
            save_notes(notes)
            print("Note edited successfully")
            return
    print("Note not found")


def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Note deleted successfully")
            return
    print("Note not found")


def filter_notes_by_date(date):
    notes = load_notes()
    filtered_notes = [note for note in notes if note["timestamp"].startswith(date)]
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")
    else:
        print("No notes found for the given date")


def main():
    while True:
        print("Commands: add, list, edit, delete, filter, exit")
        command = input("Enter the command: ").lower()

        if command == "add":
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            add_note(title, body)

        elif command == "list":
            list_notes()

        elif command == "edit":
            note_id = int(input("Enter note ID to edit: "))
            title = input("Enter new note title: ")
            body = input("Enter new note body: ")
            edit_note(note_id, title, body)

        elif command == "delete":
            note_id = int(input("Enter note ID to delete: "))
            delete_note(note_id)

        elif command == "filter":
            date = input("Enter date to filter notes (YYYY-MM-DD): ")
            filter_notes_by_date(date)

        elif command == "exit":
            break

        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()