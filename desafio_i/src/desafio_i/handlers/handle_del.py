import os
from pathlib import Path
import json
from json import JSONDecodeError
from ..shared import Person


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
