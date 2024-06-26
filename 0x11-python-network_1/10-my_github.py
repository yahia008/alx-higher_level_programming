#!/usr/bin/python3
"""
Takes my Github credentials (username and password)
and uses the Github API to display my Github id.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
Uses Basic Authentication to access the ID.
"""
import sys
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
