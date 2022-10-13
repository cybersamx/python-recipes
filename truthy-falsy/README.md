# Truthy vs Falsy

## Definition

It's straightforward when performing a logical test in a programming language when the type being evaluated is a boolean type with a value that can either be true or false - there's no room for interpretation. However there are contexts when we perform logical test using non-boolean types such as integer, string, etc. For these data values, what is interpreted as true or false (or rather truthy or falsy respectively) is predicated on how the non-boolean values are interpreted by the programming language.

## Python

This is how Python would implicitly cast a value to a boolean value. Here we force a value of any type to a boolean 
value using a conditional statement.

```python
return True if (value) else False
```

The outputs are:

| Input            | Evaluated Output |
|------------------|------------------|
| False            | False            |
| True             | True             |
| 0                | False            |
| 1                | True             |
| 0.0              | False            |
| 1.0              | True             |
| None             | False            |
| object           | True             |
| ""               | False            |
| "text"           | True             |
| '\0'             | True             |
| '\u263A'         | True             |
| []               | False            |
| [1, 2, 3]        | True             |
| {}               | False            |
| {'key': 'value'} | True             |

