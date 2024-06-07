#!/usr/bin/python3
"""A script that:
- takes in a URL and an email address
- sends a POST request to the URL with the email as a parameter,
- and finally displays the body of the response.
"""
import requests, sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)

        print(f"Error code: {response.status_code}")
    except Exception as e:
        print(e)
