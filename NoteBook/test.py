from collections import UserDict
import datetime
from colorama import Fore, Style


class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"\n{Fore.RED}Title:{Style.RESET_ALL} {self.title}\n{Fore.RED}Content: {Style.RESET_ALL} {self.content}"


class NotesBook(UserDict):
    def add_note(self, title, content):
        title += f" ({datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')})"
        note = Note(title, content)
        self.data[title] = note
        print("Note added successfully!")

    def search_notes(self, keyword):
        found_notes = []
        for note in self.data.values():  #перевіряємо чи містить заголовок або вміст ключове слово keyword.
            if keyword.lower() in note.title.lower() or keyword.lower() in note.content.lower():
                found_notes.append(note)
        if found_notes:
            print(f"{Fore.YELLOW}Found {len(found_notes)} note(s):{Style.RESET_ALL}")
            for note in found_notes:
                print(note)
                print("------------------------")
        else:
            print("No matching notes found.")

    def edit_note(self, title): # ітерація потрібна для пошуку заголовку не зважаючи на дату
        found_note = None
        for note_title in self.data.keys():
            if note_title.startswith(title): # якщо заголовок знаходиться, привласнюємо його found_note
                found_note = note_title
                break

        if found_note:
            new_content = input("Enter new content for the note: ")
            self.data[found_note].content = new_content
            print("Note updated successfully!")
        else:
            print("Note not found.")

    def delete_note(self, title):
        if title in self.data:
            del self.data[title]
            print("Note deleted successfully!")
        else:
            for key in self.data.keys():
                if key.startswith(title):
                    del self.data[key]
                    print("Note deleted successfully!")
                    return
            print("Note not found.")

    def display_all_notes(self, notes_per_page):
        if self.data:
            total_notes = len(self.data)
            total_pages = (total_notes + notes_per_page - 1) // notes_per_page
            current_page = 1
            while True:
                print(f"\n{Fore.YELLOW}Page {current_page} of {total_pages}:{Style.RESET_ALL}")
                notes_to_display = list(self.data.values())[
                    (current_page - 1) * notes_per_page: current_page * notes_per_page]
                if notes_to_display:
                    for note in notes_to_display:
                        print(note)
                        print("------------------------")
                else:
                    print("No notes found on this page.")

                if current_page < total_pages:
                    choice = input(f"Press 'Enter' to view the next page, or 'q' to quit: ")
                    if choice.lower() == "q":
                        break
                    current_page += 1
                else:
                    print("End of notes.")
                    break
        else:
            print("No notes found.")


notebook = NotesBook()


while True:
    print("\nHi,I'm a personal assistant with notes!")
    print("1. Add a note")
    print("2. Search notes")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. Display all notes")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        notebook.add_note(title, content)
    elif choice == "2":
        keyword = input("Enter a title to search notes: ")
        notebook.search_notes(keyword)
    elif choice == "3":
        title = input("Enter the title of the note to edit: ")
        notebook.edit_note(title)
    elif choice == "4":
        title = input("Enter the title of the note to delete: ")
        notebook.delete_note(title)
    elif choice == "5":
        notes_per_page = 3
        notebook.display_all_notes(notes_per_page)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

