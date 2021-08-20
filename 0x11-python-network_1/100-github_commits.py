#!/usr/bin/python3
""" a python script that takes the repository name, owner name & displys
    the most recent 10 commits
"""
import requests
import sys

if __name__ == "__main__":
    """ main method to display the most 10 recent commits """
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com"
    url_updated = "{}/repos/{}/{}/commits".format(url, owner, repo)
    c = requests.get(url_updated).json()
    try:
        for i in range(10):
            print("{}: {}".format(c[i].get('sha'),
                  c[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
