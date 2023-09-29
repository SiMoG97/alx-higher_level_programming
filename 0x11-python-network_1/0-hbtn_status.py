#!/usr/bin/python3
"""_summary_
"""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as res:
        data = res.read()
        decodedData = data.decode("UTF-8")

        print("Body response:")
        print(f"    - type: {type(data)}")
        print(f"    - content: {data}")
        print(f"    - utf8 content: {decodedData}")
