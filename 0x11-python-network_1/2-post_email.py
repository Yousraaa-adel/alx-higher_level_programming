#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(email).encode("ascii")

    try:
        request = urllib.request.Request(url, data)

        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))

    except Exception as e:
        print(e)
