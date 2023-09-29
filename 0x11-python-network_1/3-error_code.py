#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    args = sys.argv
    try:
        with urllib.request.urlopen(args[1]) as res:
            data = res.read().decode("UTF-8")
            print(data)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
