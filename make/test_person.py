import unittest

from main import Person


# This is a very test to test `make test`.
class TestPerson(unittest.TestCase):
    def test_decode(self):
        json = '{"name": "Bruce Lee", "age": 30, "username": "be_water"}'
        person = Person.from_json(json)

        self.assertEqual('Bruce Lee', person.name)
        self.assertEqual(30, person.age)
        self.assertEqual("be_water", person.username)
