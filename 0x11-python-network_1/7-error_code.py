#!/usr/bin/python3
""" a python script that takes URl & displays the body of the response
    handle the httperror
"""
import requests
import sys


if __name__ == "__main__":
    """ main method to display the content & handle error """
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
