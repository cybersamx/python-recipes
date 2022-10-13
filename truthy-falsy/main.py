#!/usr/bin/env python3

def is_truthy(val):
    return True if val else False


values = [
    False,
    True,
    0,
    1,
    0.0,
    1.0,
    None,
    object,
    "",
    "text",
    '\0',
    '\u263A',
    [],
    [1, 2, 3],
    {},
    {'key': 'value'}
]

for value in values:
    print("{0} is {1}".format(value, is_truthy(value)))
