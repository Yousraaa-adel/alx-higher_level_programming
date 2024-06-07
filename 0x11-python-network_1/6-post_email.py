#!/usr/bin/python3
"""A script that:
- takes in a URL and an email address
- sends a POST request to the URL with the email as a parameter,
- and finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    url = sys.argv[1]
    params = sys.argv[2]

    try:
        response = requests.post(url, params=params)

        print(f"Your email is: {response.text}")
    except Exception as e:
        print(e)
