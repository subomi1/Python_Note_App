import json
import os

notes_file = "notes.json"

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    return []


def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=4)


def add_notes(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    category = input("Enter category: ")   
    
    note = {
        "title": title,
        "content": content,
        "category": category
    }
    notes.append(note)
    save_notes(notes)
    print("Note added successfully")  
    
    
def view_notes(notes):
    if not notes:
        print("No notes available")
        return
    
    print("=== All notes ====")
    for index, note in enumerate(notes, start=1):
        print(f"\nNote {index}")
        print(f"Title: {note["title"]}")    
        print(f"Content: {note["content"]}")    
        print(f"Category: {note["category"]}")   
        
        
def search_notes(notes):
    category = input("Enter a keyword or category to search for: ").lower()
    found_notes = []
    
    for note in notes:
        if(
            category in note['title'].lower() or category in note['content'].lower() or category in note['category'].lower()
        ):
            found_notes.append(note)
            
        if not found_notes:
            print("No matching notes found")
        else:
            print(f"\nFound {len(found_notes)} matching notes: ")
            for index, note in enumerate(found_notes, start=1):
                print(f"\nNote {index}")
                print(f"Title: {note['title']}")
                print(f"Content: {note['content']}")
                print(f"Category: {note['category']}")
                
                
def delete_notes(notes):
    if not notes 
    view_notes(notes)
    
    for note in enumerate(notes, start=1):
                
       
        
notes = load_notes()
while True:
    print("=== Notes App ===")
    print("1. Add note")
    print("2. View all notes")
    print("3. Search notes")
    print("4. Delete note")
    print("5. Exit")
    
    option = int(input("Choose an option from (1-5): "))
    
    if option == 1:
        add_notes(notes)
    elif option == 2:
      view_notes(notes)
    elif option == 3:
        search_notes(notes)
    elif option == 4:
        
        