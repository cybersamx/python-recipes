#!/usr/bin/env python3

import unicodedata

# Unicode representation
print('a' == '\x61')
print('a' == '\u0061')
print('a' == '\U00000061')

# Python3 supports supplementary Unicode code point directly.

# Full supplementary code point => true
print('๐' == '\U0001F44D')
# Surrogate pair code points => true
print('๐' == '\uD83D\uDC4D'.encode('utf-16', 'surrogatepass').decode('utf-16'))
# Literal comparison
print('๐' == '๐')

# Extended grapheme cluster
# Both prints print the same character รก
print('\u00E1')                     # Prints รก using a precomposed รก
print('\u0061\u0301')               # Prints รก using a decomposed combo of a, โฬ

# Here's the kicker
print('\u00E1' == 'รก')              # True
print('\u0061\u0301' == 'รก')        # False
print('\u00E1' == '\u0061\u0301')   # False

# The fix: normalization
print('\u0061\u0301' == unicodedata.normalize('NFD', '\u00E1'))  # True
print(unicodedata.normalize('NFC', '\u0061\u0301') == '\u00E1')  # True
