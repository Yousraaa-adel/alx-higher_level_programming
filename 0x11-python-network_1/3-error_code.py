#!/usr/bin/python3
"""A script that:
- takes in a URL,
- displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    try:
        # request = urllib.request.Request(url)

        with urllib.request.urlopen(url) as response:
            print(response.read().decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
