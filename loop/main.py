#!/usr/bin/env python3

import sys

numbers = [9, 8, 7]
size = len(numbers)

# While loop.
j = 0
while j < size:
    print(numbers[j], end=' ')     # Prints 9, 8, 7
    j += 1
print()

# For-in loop using range.
for i in range(0, size):
    print(numbers[i], end=' ')     # Prints 9, 8, 7
print()

for i in range(size):              # Shorthand
    print(numbers[i], end=' ')     # Prints 9, 8, 7
print()

# For-in loop using xrange.
if sys.version_info[0] < 3:
    for i in xrange(size):
        print(numbers[i], end=' ')  # Prints 9, 8, 7
print()

# For-in-else loop.
for i in range(size):
    print(numbers[i], end=' ')
else:
    print(numbers[i], end=' ')     # Prints 9, 8, 7, 7
print()

# For-in loop.
for n in numbers:
    print(n, end=' ')              # Prints 9, 8, 7
print()

# For-in works on string.
text = 'hello'
for n in text:
    print(n, end=' ')              # Prints h, e, l, l, o
print()
