#!/usr/bin/python3
""" a python script that takes a letter & search the letter
    handle the httperror
"""
import requests
import sys


if __name__ == "__main__":
    """ main method that takes a letter & searchs a given letter """
    if len(sys.argv) <= 1:
        letter = ""
    else:
        letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    values = {"q": letter}
    req = requests.post(url, data=values)
    try:
        cnt = req.json()
        if cnt == {}:
            print("No result")
        else:
            print("[{}] {}".format(cnt.get("id"), cnt.get("name")))
    except ValueError:
            print("Not a valid JSON")
