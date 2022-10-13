#!/usr/bin/env python3

operandsA = {
    'True': True,
    'False': False,
    '1': 1,
    '0': 0,
    '-1': -1,
    '1.0': 1.0,
    '0.0': 0.0,
    '-1.0': -1.0,
    '"True"': 'True',
    '"False"': 'False',
    '"1"': '1',
    '"0"': '0',
    '"-1"': '-1',
    '"0.0"': '0.0',
    '"1.0"': '1.0',
    '"-1.0"': '-1.0',
    '""': '',
    '"\\u0000"': '\u0000',
    'None': None,
    'Infinity': float('inf'),
    '-Infinity': -float('inf'),
    '[]': [],
    '{}': {},
    '[[]]': [[]],
    '[0]': [0],
    '[1]': [1],
    '[0, 1]': [0, 1],
    '[[0]]': [[0]],
    '[[1]]': [[1]],
    '[[0, 1]]': [[0, 1]],
    '{"a": "b"}': {"a": "b"},
    'NaN': float('NaN')
}

operandsB = {
    'True': True,
    'False': False,
    '1': 1,
    '0': 0,
    '-1': -1,
    '1.0': 1.0,
    '0.0': 0.0,
    '-1.0': -1.0,
    '"True"': 'True',
    '"False"': 'False',
    '"1"': '1',
    '"0"': '0',
    '"-1"': '-1',
    '"0.0"': '0.0',
    '"1.0"': '1.0',
    '"-1.0"': '-1.0',
    '""': '',
    '"\\u0000"': '\u0000',
    'None': None,
    'Infinity': float('inf'),
    '-Infinity': -float('inf'),
    '[]': [],
    '{}': {},
    '[[]]': [[]],
    '[0]': [0],
    '[1]': [1],
    '[0, 1]': [0, 1],
    '[[0]]': [[0]],
    '[[1]]': [[1]],
    '[[0, 1]]': [[0, 1]],
    '{"a": "b"}': {"a": "b"},
    'NaN': float('NaN')
}

print('== operator...')
print('--------------')
for text_a, operand_a in operandsA.items():
    for text_b, operand_b in operandsB.items():
        result = operand_a == operand_b
        if result:
            print("{0}, {1}".format(text_a, text_b))

print('is operator...')
print('--------------')
for text_a, operand_a in operandsA.items():
    for text_b, operand_b in operandsB.items():
        result = operand_a is operand_b
        if result:
            print("{0}, {1}".format(text_a, text_b))
