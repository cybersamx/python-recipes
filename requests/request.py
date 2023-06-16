#!/usr/bin/env python

import requests


res = requests.request(method='GET', url='https://httpstat.us/200')

print(res.status_code)
print(res.text)
