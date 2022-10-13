# Variable

## Declaration

```python
# No constant construct in Python, use uppercase letters to denote constant.
PI = 3.141
message = 'hello'
```

## Null Coalescing Operator

Returns or assigns the first value of the first operand if it exists and not falsy - and different programming language define falsy different. See [truthy vs falsy](../truthy-falsy) for details.

```python
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
```

## Ternary Conditional Assignment

```python
# Ternary conditional assignment.
x = 7
oversize = True if (x > 5) else False
print(oversize)   # Prints true
oversize = (False, True)[x > 5]
print(oversize)   # Prints true
```

# Reference

* [Wikipedia: Null Coalescing Operator](https://en.wikipedia.org/wiki/Null_coalescing_operator)
