#!/usr/bin/python3

from urllib.request import urlopen
import sys

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
