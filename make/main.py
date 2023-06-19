import json
import os
from pathlib import Path
from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class Person(JSONWizard):
    name: str
    age: int
    username: str


def main():
    filename = os.path.join(Path.cwd(), 'sample.json')
    with open(filename) as file:
        data = json.load(file)

    person = Person.from_dict(data)
    print(person)


if __name__ == '__main__':
    main()
