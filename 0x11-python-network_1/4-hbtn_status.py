#!/usr/bin/python3
""" a python script that feteches intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    """ main method to fetche intranet.hbtn.io """
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
