#!/usr/bin/python3

import urllib.request
from urllib.request import urlopen

try:
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        data = response.read()
        content = data.decode()

        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {content}")
except Exception as e:
    print(e)
