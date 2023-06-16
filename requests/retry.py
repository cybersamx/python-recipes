#!/usr/bin/env python
# CREDIT: https://stackoverflow.com/questions/23267409/how-to-implement-retry-mechanism-into-python-requests-library

import logging
import requests
from requests.adapters import HTTPAdapter, Retry

logging.basicConfig(level=logging.DEBUG)

s = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
s.mount('https://', HTTPAdapter(max_retries=retries))

res = s.get('https://httpstat.us/503')
