#!/usr/bin/python3
"""
    a script that takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""
import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    with requests.get(args[1]) as res:
        print(res.headers["X-Request-Id"])
