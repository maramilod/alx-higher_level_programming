#!/usr/bin/pyhon3
"""hey"""
import requests
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(
        f"https://api.github.com/user/{username}",
        auth=(username, password),
        headers=headers
    )

    if response.status_code == 200:
        print(response.json().get('id', None))
    else:
        print(None)


if __name__ == "__main__":
    main()
