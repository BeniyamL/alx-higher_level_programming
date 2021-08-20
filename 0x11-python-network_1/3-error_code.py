#!/usr/bin/python3
""" a python script that takes URl & displays the value of x-Request-Id
    handle the httperror
"""
import urllib.request
import sys


if __name__ == "__main__":
    """ main method to display the content & handle error """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
