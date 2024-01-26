#!/usr/bin/python3
"""hey"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')

status_code = response.status_code
content = response.text

print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
