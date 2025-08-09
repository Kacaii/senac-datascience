from json.decoder import JSONDecodeError
import os
import sys
import json
from pathlib import Path
from typing import TypedDict

help_message = """
Usage:
    
    $ <python> src/desafio_i/main.py [add,del] <json path>

Args:

    add     add a person to the list
    del     removes a person from the list
"""


class Person(TypedDict):
    name: str
    phone: str
    email: str


## Starting point.
def main():
    if len(sys.argv) < 3:
        print(help_message)

        # Returns safely if there is no args or json path.
        return

    json_path = sys.argv[2]

    match sys.argv[1]:
        case "del":
            handle_remove(json_path)
        case _:
            print(help_message)


def append_person_to_json(json_path: str, person: Person):
    """
    Opens an arbitrary `json` file using the current diretory as reference and
    appends a person to it
    """

    current_dir = Path().cwd()
    data_path = os.path.join(current_dir, json_path)

    with open(data_path, "r") as file:
        data: list[Person] = json.load(file)

        data.append(person)

        file.seek(0)
        json.dump(data, file)


def handle_remove(json_path: str):
    email = input(
        "Please enter the email you would like to remove from the list:\n  -> "
    )

    match remove_person_from_json(json_path, email):
        # I could use an `if else`, but I REALLY like switch statements.
        case True:
            print(email, "was removed successfully from the list! ")
        case False:
            print(email, "was not removed on the list. 󱆥")


def remove_person_from_json(json_path: str, email: str) -> bool:
    """
    Opens an arbitrary `json` file using the current diretory as reference and
    removes a person from it by their email
    """

    current_dir = Path().cwd()
    data_path = os.path.join(current_dir, json_path)

    # Error handling is important.
    try:
        with open(data_path, "r") as file:
            data: list[Person] = json.load(file)
    except JSONDecodeError:
        print("Failed to decode data from the json file. 󰘦")
        return False
    except FileNotFoundError:
        print("Failed to locate the data file. 󱔼")
        return False

    # Filter everyone that doesnt have the passed email string.
    updated_data = [person for person in data if person.get("email") != email]

    # Run this if someone got filtered.
    if len(updated_data) < len(data):
        try:
            with open(data_path, "w") as file:
                json.dump(updated_data, file)

            # Return true if the person was removed successfully.
            return True
        except JSONDecodeError:
            print("Failed to decode data from the json file. 󰘦")
            return False
        # Just in case someone inputs a file that doesnt exist.
        except FileNotFoundError:
            print("Failed to locate the data file. 󱔼")
            return False

    # Return false if the person was not removed.
    print("The email is not on the list, maybe you missed a character?")
    return False


# Starting execution 
if __name__ == "__main__":
    main()
