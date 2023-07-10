import pickle
from my_classes import *
from parser_oop import Command
from search import search, bday_people


# Define break points and available commands
BREAK_POINTS = {"good bye", "close", "exit"}

# storage details; save on exit
storage_name = "AdressBook\data.bin"

try:
    with open(storage_name, "rb") as fh:
        unpacked = pickle.load(fh)
except EOFError:
    unpacked = AddressBook()
except FileNotFoundError:
    unpacked = AddressBook()

DATA = unpacked

# for the function 'page'
number_of_cntacts_on_page = 2


# Decorator for handling input errors
def input_error(func):
    """Decorator that handles common input errors for command functions."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact!"
        except ValueError as msg:
            return f"{msg}"
        except TypeError as msg:
            return f"{msg}"

    return inner


# Command functions
@input_error
def hello(*_):
    """Greet the user."""

    return "How can I help you? Type 'help' to see list of available commands \n "


@input_error
def help(*_):
    """Show a list of available commands and their usage."""

    list_of_instructions = [
        "The order of input matters; only commands and names are strictly required;\nnumbers must not contain spaces \n",
        "1. greeting: hello",
        "2. adding or updating a contact: add name -number -additional numbers --birthday dd/mm(/yyyy)",
        "3. completely modify an existing contact: change name -number --birthday",
        "4. number(s): call name",
        "5. removes the contact entirely: remove name",
        "6. reveal the data: show_all",
        "7. pagination with default value 2 record per page: page",
        "8. days to birthday: bday name",
        "9. show all available commands: help",
        f"10. to exit the program and save changes: {' or '.join(list(BREAK_POINTS))} ",
        "11. to search through the data: search",
        "12. to see the list of people who have bdays in some days: bdays number_of_days",
    ]

    return "\n".join(list_of_instructions)


@input_error
def add(name, phones, bday=None):
    """Add a new contact to the data."""

    if name in DATA.data.keys():
        new_phones_list = []
        for num in phones:
            phone_object = Phone()
            phone_object.value = num
            new_phones_list.append(phone_object)
        DATA[name].add_phones(new_phones_list)

        if bday:
            bday_object = Birthday()
            bday_object.value = bday
            DATA[name].add_bday(bday_object)
        return "the contact is now updated and will be saved on exit; to view changes now, use 'show_all command'"

    else:
        name_object = Name()
        name_object.value = name
        new_phones_list = []
        for num in phones:
            phone_object = Phone()
            phone_object.value = num
            new_phones_list.append(phone_object)
        record = Record(name_object, new_phones_list)
        if bday:
            bday_object = Birthday()
            bday_object.value = bday
            record = Record(name_object, new_phones_list, bday=bday_object)
        result = DATA.add_record(record)
        return result


@input_error
def change(name, phones, bday=None):
    """Change the phone number for an existing contact."""
    new_phones_list = []
    for num in phones:
        phone_object = Phone()
        phone_object.value = num
        new_phones_list.append(phone_object)
    DATA[name].change_phones(new_phones_list)
    if bday:
        bday_object = Birthday()
        bday_object.value = bday
        DATA[name].change_bday(bday_object)
    return "the contact is now updated"


@input_error
def call(name, *_):
    """Show the phone number(s) for a contact."""
    list_of_contacts = [i.value for i in DATA.data[name].phones]
    return f"{name}'s number is {', or '.join(list_of_contacts)}"


@input_error
def remove(name, *_):
    """Deletes the contact."""
    for i in DATA.data.keys():
        if i == name:
            DATA.delete_record(DATA[i])
            return "done!"
    return "no such record!"


@input_error
def show_all(*_):
    """Show all contacts in the data."""
    result = ""
    for i, j in DATA.data.items():
        if j.bday:
            if j.bday.value:
                result += f'{i}:{", ".join(k.value for k in j.phones)}, and birthday is {j.bday.value}!'
        else:
            result += f'{i}:{", ".join(k.value for k in j.phones)}'
        result += "\n"
    return result


@input_error
def bday(name, *_):
    return DATA.data[name].days_to_birthday()


# Set of command functions, but it doesn't include pagination 'page' and exit points
commands = {
    "hello": hello,
    "add": add,
    "change": change,
    "call": call,
    "remove": remove,
    "show_all": show_all,
    "help": help,
    "bday": bday,
    "search": search,
}


# Main loop
@input_error
def main():
    """Main function that runs the program."""
    while True:
        user_input = input("> ")

        if user_input in BREAK_POINTS:
            break

        c = Command(user_input)
        if c.command == "add":
            if c.name:
                result = add(c.name, c.phones, bday=c.bday)
                print(result)
            else:
                print("name required!")
        elif c.command == "change":
            result = change(c.name, c.phones, bday=c.bday)
            print(result)

        elif c.command == "page":
            it = DATA.iterator(number_of_cntacts_on_page)
            while True:
                inp = input(
                    'type "b" to stop scrolling and go back, press enter to see the next page\n'
                ).strip()
                if inp == "b":
                    break
                elif it.page_counter >= it.max_pages:
                    print("the end!")
                    break

                page = next(it)
                print(page)

        elif c.command == "search":
            while True:
                pattern = input(
                    'please specify your search pattern or enter "b" to quit search: '
                )
                if pattern.strip() == "b":
                    break
                else:
                    print(search(pattern, DATA))

        elif re.search(r"bdays \d+", user_input):
            print(bday_people(DATA, re.search(r"\d+", user_input).group()))

        else:
            command, *data = c.command, c.name, c.phones
            if func := commands.get(command):
                print(func(*data))

            else:
                print("No such command! To see available list of commands type 'help' ")

    print("Good bye!")


if __name__ == "__main__":
    main()
    with open(storage_name, "wb") as fh:
        pickle.dump(DATA, fh)