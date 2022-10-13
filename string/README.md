# String

## String Literal

### String Quote

How are string literal represented in various languages.

| Language   | Single Quote | Double Quote |
|------------|--------------|--------------|
| Javascript | yes          | yes          |
| Python     | yes          | yes          |
| Bash       | yes          | yes          |
| Go         | no           | yes          |

## Unicode Representation

Unicode is a large lookup database of glyphs and symbols, which can be individually be referenced by a Unicode symbol can be referenced by a `code point`.

The naming convention of a `Unicode code point` is `U+XXXX` where XXXX is zero-padded hexadecimal number ranging from `0000` to `FFFF`, which is also known as the **Basic Multilingual Plane (BMP)**. It was designed to be 16-bit encoding; but the initial set of 65,536 distinct symbols quickly ran out and the Unicode consortium extended the Unicode set by another 1+ million symbols with the addition of 2 digits. Known as the **Supplementary Plane (SP)**, the characters in the extended set are in the range U+010000 to U+10FFFF. Read [here](https://en.wikipedia.org/wiki/Unicode) for more information on Unicode.

BMP code point can be accessed as a single code unit in UTF-16 encoding ie. basically a 16-bit data type to represent a Unicode character from U+0000 to U+FFFF. However a SP code point is 21-bit and a UTF-32 encoded string would end up wasting a lot of space. Most programming language uses UTF-16 encoding in its string representation, which makes sense since UTF-32 will be space inefficient. A 21-bit supplementary character is represented by a pair of surrogate 16-bit code points in a UTF-16 encoded string environment. For instance the symbol 👍 is U+1F44D but it can also be represented as U+D83D and U+DC4D (encoded in UTF-16) - in fact, some languages represents the a SP code point as surrogate pairs internally.

> **Note**
> As you can see, any number in the BMP code point in the range of U+0000 to U+D7FF and U+D7FF and U+E000 to U+10FFFF represents a Unicode character. A code point in range U+D800 to U+D7FF represents a surrogate part code point.

| Name                      | Lower range | Upper range |
|---------------------------|-------------|-------------|
| Basic Multilingual Plane  | U+0000      | U+FFFF      |
| Surrogate Pair Code Point | U+D800      | U+DFFF      |
| Supplementary Plane       | U+100000    | U+10FFFF    |


### Javascript

```javascript
// Unicode representation
console.log('a' === '\x61');
console.log('a' === '\u0061');              // Without the {}, code point be 4 digits.
console.log('a' === '\u{61}');              // With the {}, the code point can be 1-6 digits.

// ES6 supports supplementary Unicode code point directly.
console.log('👍' === '\u{1F44D}');          // Full supplementary code point => true
console.log('👍' === '\u{D83D}\u{DC4D}');   // Surrogate pair code points => true

// Extended grapheme cluster
console.log("\u{E1}");                      // Prints á using a precomposed á
console.log("\u{61}\u{301}");               // Prints á using a decomposed combo of a, ◌́
```

### Python

```python
# Unicode representation
print('a' == '\x61')
print('a' == '\u0061')
print('a' == '\U00000061')

# Python3 supports supplementary Unicode code point directly.
print('👍' == '\U0001F44D')           # Full supplementary code point => true
```

See [unicode.py](unicode.py) for details.

### Go

```go
// Hex representation
fmt.Println("a" == "\x61")

// Unicode representation
// Use escape \u followed by 4 digit unicode code point.
// Use escape \U followed by 8 digit unicode supplementary code point
fmt.Println("a" == "\u0061")

// Go supports supplementary Unicode code point directly.
// Surrogate pair code points is unsupported,
// ie. print("👍" == "\u{D83D}\u{DC4D}") doesn't work.
fmt.Println("👍" == "\U0001F44D")

// Extended grapheme cluster
fmt.Println("\u00E1")         // Prints á using a precomposed á
fmt.Println("\u0061\u0301")   // Prints á using a decomposed combo of a, ◌́
```

### Unicode Escape Sequence

The different formats of escape sequences in various programming languages.

| Escape Sequence                                     | Javascript         | Python         | Bash           | Go           |
|-----------------------------------------------------|--------------------|----------------|----------------|--------------|
| Hexadecimal Escape Seq eg. 'a'                      | '\x61'             | '\x61'         | '\x61'         | "\x61"       |
| Unicode Escape Seq eg. 'a'                          | '\u0061'           | '\u0061'       | N/A            | "\u0061"     |
| Supplementary Unicode eg. '👍'                      | '\u{1F44D}'        | '\U0001F44D'   | '\x61\xCC\x81' | "\U0001F44D" |
| Supplementary Unicode using surrogate pair eg. '👍' | '\u{D83D}\u{DC4D}' | '\uD83D\uDC4D' | '\x61\xCC\x81' | N/A          |

* In Python `\u` means 16-bit scalar Unicode value and `\U` 32-bit Unicode scalar value
* Can't use supplementary unicode code point values in Java string escape sequences, use surrogate pairs instead

## String Interpolation

```python
name = 'sam'
print("hello %s" % name)   # Use %d for numerical value
print("hello {0}".format(name))
print("hello {text}".format(text=name))
```

See [PyFormat](https://pyformat.info/) for detailed formatting specifiers and examples on the C printf-style and .format style string interpolation.

## References

* [Javascript has a unicode problem](https://mathiasbynens.be/notes/javascript-unicode)
* [Python3 Unicode](https://docs.python.org/3/howto/unicode.html)
* [Wikipedia: Unicode](https://en.wikipedia.org/wiki/Unicode)
