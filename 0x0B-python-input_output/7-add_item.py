#!/usr/bin/python3
""" A Moule that  """
from sys import argv


# Importing save_to_json_file and load_from_json_file
save_file = __import__("5-save_to_json_file.py").save_to_json_file
load_file = __import__("6-load_from_json_file.py").load_from_json_file

try:
    json_list = load_file("add_item.json")
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save_file(json_list, "add_item.json")
