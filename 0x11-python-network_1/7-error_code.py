#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""
import requests
import sys

if __name__ == "__main__":
    args = sys.argv
    try:
        res = requests.get(args[1])
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
