#!/bin/bash
# Send a request to the URL and save the output to a temporary file
curl -I "$1" -s | grep Content-Length | cut -d ' ' -f2
