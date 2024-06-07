#!/usr/bin/python3
"""A script that:
- takes in my GitHub credentials
- and uses the GitHub API to display my id
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    headers = {
        "Authorization": "token {}".format(
            token
        ),
    }

    try:
        # Fetching information about the specified user using GET
        response = requests.get("https://api.github.com/users/{}".format(
            username), headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            print(user_data["id"])
        else:
            print(None)

    except Exception as e:
        print(e)
