#!/usr/bin/python3
"""Executes a POST request to a specified
URL with a given email.

Usage: ./2-post_email.py <URL> <email>
Shows the response body.
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
