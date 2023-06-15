#!/usr/bin/env python3

from time import time
from dataclasses import dataclass, field
from typing import ClassVar, Optional, Type, TypeVar
from faker import Faker
from random import randint

T = TypeVar('T')
Faker.seed(time())
fake = Faker()


# Immutable class if frozen == True.
@dataclass(frozen=True)
class Person(object):
    # Class variables
    mean_age: ClassVar[int] = 30
    vocabulary: ClassVar[list[str]] = ['hello', 'bye', 'thank you', 'welcome']

    # Instance variables
    first_name: str
    last_name: str
    note: str = field(default="Nothing", repr=False)  # This field will not be printed.
    age: int = field(default=20)
    middle_name: Optional[str] = None

    @classmethod
    # We don't have to do this, but if we want to be strict about typing.
    def random_person(cls: Type[T]) -> T:
        # A class method can modify the class state.
        rand_age = randint(15, 45)
        cls.mean_age = int((15+45+rand_age)/3)

        return Person(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=rand_age
        )

    @staticmethod
    def is_adult(age) -> bool:
        # Static methods are basically functions.
        return age > 18

    def talk(self) -> str:
        i = randint(0, 3)
        return f'{self.first_name} says {Person.vocabulary[i]}'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, aged {self.age}"


def main():
    # Initialize
    john = Person(
        first_name="John",
        last_name="Lee",
        note="Student in 2C"
    )
    print(john)
    print(john.talk())

    # Class method and variable
    print(Person.mean_age)

    random = Person.random_person()
    print(random)

    print(Person.mean_age)

    # Static methods
    age = 25
    print(f'Age {age} is an adult: {Person.is_adult(age)}')


if __name__ == '__main__':
    main()
