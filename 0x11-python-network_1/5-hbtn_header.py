#!/usr/bin/python3
""" Takes in a URL, send a request and displays
the value of the variable X-Request-ID
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)

    print(req.headers.get("X-Request-Id"))
