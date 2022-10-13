#!/usr/bin/env python3

def foo(x):
    return x or 'hello'


# Return the default value if x is falsy.
x = None
print(foo(x))   # x is None, prints default value 'hello'.
x = ''
print(foo(x))   # x is an empty string, prints default value 'hello'.

# Return x if it's set to a value.
x = 'bye'
print(foo(x))   # x has a value, prints x.

# Python also has a syntax where x = (if_false, if_true)[condition]
a = 10
b = 5
x = (a, b)[a > b]
print(x)        # Prints 5
