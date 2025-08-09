from pathlib import Path
import os
import sys
import json
from .handlers.handle_del import handle_remove
from .shared import Person


help_message = """
Usage:
    
    $ <python> src/desafio_i/main.py [add,del] <json path>

Args:

    add     add a person to the list
    del     removes a person from the list
"""


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


# Starting execution 
if __name__ == "__main__":
    main()
