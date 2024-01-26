#!/usr/bin/python3
"""hey"""
import sys
import urllib.request


def main():
    try:
        with urllib.request.urlopen(sys.argv[1]) as url:
            headers = dict(url.info())
            print(headers['X-Request-Id'])
    except Exception as e:
        print("An error occurred: {}".format(str(e)))


if __name__ == "__main__":
    main()
