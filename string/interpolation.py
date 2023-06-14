#!/usr/bin/env python3

name = 'sam'
print("hello %s" % name)   # C printf style format
print("hello {0}".format(name))
print("hello {text}".format(text=name))
print(f"hello {name}")      # f-string supported on python 3.6+
