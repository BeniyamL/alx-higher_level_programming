#!/usr/bin/python3
""" a python script that takes URl & displays the value of x-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    """ main method to display the x-Request-Id value """
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
