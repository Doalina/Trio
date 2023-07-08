import os

def print_menu():
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
    print("║                   EXIT                         ║")
    print("║                                                ║")
    print("╚════════════════════════════════════════════════╝")

def run_address_book():
    os.system("python3 AdressBook/test.py")

def run_folder_sorter():
    os.system("python3 FolderSorter/test.py")

def run_note_book():
    os.system("python3 NoteBook/test.py") 

def main_menu():
    while True:
        print_menu()
        choice = input("You are in \"MAIN MENU\". Choose one of the options: \n>>> ")

        if choice == "1":
            run_address_book()
            input("Press enter to continue.")

        elif choice == "2":
            run_folder_sorter()
            input("Press enter to continue.")

        elif choice == "3":
            run_note_book()
            input("Press enter to continue.")

        elif choice.lower() == "exit":
            print("Exit")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
