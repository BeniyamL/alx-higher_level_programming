#!/usr/bin/python3
""" take a URL, email & send a POST request to the passed URL """
import requests
import sys


if __name__ == "__main__":
    """ main method to accept and send a POST request """
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    req = requests.post(url, data=values)
    print(req.text)
