#!/usr/bin/python3
import urllib.request

try:
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as url:
        f = url.read()
        print("Body response:")
        print("\t- type: {}".format(type(f)))
        print("\t- content: {}".format(f))
        print("\t- utf8 content: {}".format(f.decode()))
except Exception as e:
    print("An error occurred: {}".format(str(e)))

