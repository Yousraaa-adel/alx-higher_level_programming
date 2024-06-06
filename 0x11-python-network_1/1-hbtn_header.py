#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""

from urllib.request import urlopen
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urlopen(url) as response:
            content = response.read()

            X_Request_Id = response.getheader("X-Request-Id")
            print(X_Request_Id)
    except Exception as e:
        print(e)
