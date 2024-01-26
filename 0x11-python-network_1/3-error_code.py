#!/usr/bin/python3
"""hey"""
import sys
import urllib.request
from urllib.error import HTTPError


def main():
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as url:
            f = url.read()
            print(f.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
