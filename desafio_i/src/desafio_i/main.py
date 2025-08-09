import os
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Person:
    name: str
    phone: str
    email: str


def main():
    current_dir = Path().cwd()
    data_path = os.path.join(current_dir, "src/data.json")

    with open(data_path) as file:
        data = json.load(file)

    print(data)


# Starting execution 
if __name__ == "__main__":
    main()
