#!/usr/bin/python3
""" take a URL, email & send a POST request to the passed URL """
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    """ main method to accept and send a POST request """
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
