from ..shared import Person
import json
from json import JSONDecodeError


def handle_listing(data_path: str):
    try:
        with open(data_path, "r") as file:
            data: list[Person] = json.load(file)
            for person in data:
                print("╒═", person["name"])
                print("├─", person["phone"])
                print("└─", person["email"])

    except JSONDecodeError:
        print("Failed to decode data from the json file. 󰘦")
        return False
    except FileNotFoundError:
        print("Failed to locate the data file. 󱔼")
        return False
