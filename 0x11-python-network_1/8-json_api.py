#!/usr/bin/python3
"""hey"""
import requests
import sys
import json


def main():
    url = "http://0.0.0.0:5000/search_user"
    q = ""

    if len(sys.argv) > 1:
        q = sys.argv[1]

    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        json_response = json.loads(response.text)

        if json_response:
            for user in json_response:
                print("[{}] {}".format(user['id'], user['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
