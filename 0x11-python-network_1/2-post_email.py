#!/usr/bin/python3
"""
    a Python script that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and displays the body
    of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    args = sys.argv
    data_encoded = urllib.parse.urlencode({'email': args[2]}).encode("utf-8")
    request = urllib.request.Request(args[1], data_encoded, method="POST")
    with urllib.request.urlopen(request) as res:
        data = res.read().decode("UTF-8")
        print(data)
