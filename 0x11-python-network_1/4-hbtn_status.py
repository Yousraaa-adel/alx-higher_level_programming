#!/usr/bin/python3
"""A script that:
- takes in a URL,
- displays the body of the response (decoded in utf-8)
"""
import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
