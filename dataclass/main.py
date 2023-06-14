#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import Optional


# Immutable class if frozen == True.
@dataclass(frozen=True)
class Person(object):
    first_name: str
    last_name: str
    note: str = field(default="Nothing", repr=False)  # This field will not be printed.
    age: int = field(default=20)
    middle_name: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, aged {self.age}"


def main():
    john = Person(
        first_name="John",
        last_name="Lee",
        note="Student in 2C"
    )

    print(john)


if __name__ == '__main__':
    main()



