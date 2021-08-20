#!/usr/bin/python3
""" a python script that takes github credentials & uses the Github API
    to display the id number
"""
import requests
import sys

if __name__ == "__main__":
    """ main method to display the github user id """
    username = sys.argv[1]
    password = sys.argv[2]
    auth_basic = (username, password)
    url = "https://api.github.com/user"
    req = requests.get(url, auth=auth_basic)
    print(req.json().get("id"))
