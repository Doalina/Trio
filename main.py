import os

def print_menu():
    print("You are in \"MAIN MENU\". Choose one of the options:")
    print("╔════════════════════════════════════════════════╗")
    print("║                                                ║")
    print("║                 MAIN MENU                      ║")
    print("║                                                ║")
    print("╠────────────────────────────────────────────────╣")
    print("║          1. ADDRESS BOOK MENU                  ║")
    print("╠────────────────────────────────────────────────╣")
    print("║          2. FOLDER SORTER MENU                 ║")
    print("╠────────────────────────────────────────────────╣")
    print("║          3. NOTE BOOK MENU                     ║")
    print("╠────────────────────────────────────────────────╣")
    print("║                                                ║")
    print("║          4.        EXIT                        ║")
    print("║                                                ║")
    print("╚════════════════════════════════════════════════╝")

def run_address_book():
    os.system("python AdressBook/bot.py")

def run_folder_sorter():
    os.system("python FolderSorter/bot.py")

def run_note_book():
    os.system("python NoteBook/bot.py")

def main_menu():
    while True:
        print_menu()
        choice = input("\n>>> ")

        if choice == "1":
            run_address_book()

        elif choice == "2":
            run_folder_sorter()

        elif choice == "3":
            run_note_book()

        elif choice.lower() == "4":
            print("Exit")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
