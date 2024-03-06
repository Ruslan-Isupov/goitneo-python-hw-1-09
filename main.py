# HW1
# 1 task
from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):

    dict_birthday = defaultdict(list)

    today = datetime.today().date()

    for user in users:

        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        else:
            delta_days = (birthday_this_year - today).days
            precise_day = birthday_this_year.weekday()

            if delta_days < 7 and precise_day <= 4:
                day_of_week = birthday_this_year.strftime("%A")
                dict_birthday[day_of_week].append(name)

            elif delta_days < 7 and precise_day > 4:
                day_of_week = "Monday"
                dict_birthday[day_of_week].append(name)

            else:
                continue

    for name, birthday in dict_birthday.items():
        info_birthdays = ", "
        print(f"{name}: {info_birthdays.join(birthday)}")


# print(
#     get_birthdays_per_week(
#         [
#             {"name": "Johny Cash", "birthday": datetime(1955, 10, 28)},
#             {"name": "Billie Eilish", "birthday": datetime(1955, 2, 28)},
#             {"name": "Bill Gates", "birthday": datetime(1975, 3, 6)},
#             {"name": "Andrew Taco", "birthday": datetime(1985, 3, 5)},
#             {"name": "Will Smith", "birthday": datetime(1995, 3, 9)},
#             {"name": "Jaret Stivenson", "birthday": datetime(1998, 3, 10)},
#         ]
#     )
# )


# Task 2


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        return "This name doesn't exist"


def show_phone(args, contacts):
    (name,) = args
    if name in contacts.keys():
        return contacts.get(name)
    else:
        return "This name doesn't exist"


def show_all(contacts):
    info_contacts = ""
    for name, phone in contacts.items():
        info_contacts += f"{name}:{phone}\n"
    if info_contacts:
        return info_contacts.strip()
    else:
        return "We don't have any contacts"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
