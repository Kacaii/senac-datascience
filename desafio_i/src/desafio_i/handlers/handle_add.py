from ..shared import Person
from json import JSONDecodeError
import json


def handle_append(data_path: str):
    name = input("Please enter your name:\n > ")
    phone = input("Please enter your phone number:\n > ")
    email = input("Please enter your email:\n > ")

    person = Person(
        name=name,
        phone=phone,
        email=email,
    )

    match append_person_to_json(data_path, person):
        case True:
            print(person["name"], "was registred successfully!")
        case False:
            print("Failed to add", person["name"])


def append_person_to_json(data_path: str, person: Person) -> bool:
    try:
        with open(data_path, "r") as file:
            data: list[Person] = json.load(file)
    except JSONDecodeError:
        print("Failed to decode data from the json file. 󰘦")
        return False
    except FileNotFoundError:
        print("Failed to locate the data file. 󱔼")
        return False

    match person in data:
        case True:
            print(person["name"], "is already on the list")
            return False
        case False:
            pass

    data.append(person)

    try:
        with open(data_path, "w") as file:
            json.dump(data, file)
        return True
    except JSONDecodeError:
        print("Failed to decode data from the json file. 󰘦")
        return False
    except FileNotFoundError:
        print("Failed to locate the data file. 󱔼")
        return False
