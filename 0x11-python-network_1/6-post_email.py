#!/usr/bin/python3
"""
    a Python script that takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and displays the body
    of the response (decoded in utf-8)
"""
import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    data = {'email': args[2]}
    res = requests.post(args[1], data)
    print(res.text)
