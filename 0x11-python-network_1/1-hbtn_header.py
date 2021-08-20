#!/usr/bin/python3
""" a python script that takes URl & displays the value of x-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    """ main method to display the x-Request-Id value """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        hdr = res.headers
        print(dict(hdr).get('X-Request-Id'))
