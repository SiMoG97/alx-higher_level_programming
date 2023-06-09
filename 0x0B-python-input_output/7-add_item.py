#!/usr/bin/python3
"""add_item"""
import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    args = list(sys.argv[1:])

    data = []
    if os.path.isfile(filename):
        data = list(load_from_json_file(filename))

    data.extend(args)
    save_to_json_file(data, filename)
