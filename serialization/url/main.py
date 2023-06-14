#!/usr/bin/env python3

from urllib.parse import urlencode, urlparse, urlunparse
from collections import namedtuple

queries = {
    "referrer": "Snapchat",
    "action": "sign-in",
    "date": "2023-05-10",
}

# For details, read: https://docs.python.org/3/library/urllib.parse.html

UrlComponents = namedtuple(
    typename="NetLocComponents",
    field_names=["scheme", "netloc", "path", "params", "query", "fragment"],
)

# We can also pass a list to urlunparse. Let's stick with more structured means
# to keep the code robust.
url = urlunparse(
    UrlComponents(
        scheme="https",
        netloc="example.com:8000",
        path="/api/v1/blogs",
        params="article1",
        query=urlencode(queries),
        fragment="bookmark",
    )
)

print(url)

url = "https://docs.python.org:443/3/library/urllib.parse.html#structured-parse-results"

print(urlparse(url))
