#!/usr/bin/python3
""" documentation """
import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file')\
    .load_from_json_file


if os.path.exists('add_item.json'):
    loadFile = load_from_json_file('add_item.json')
else:
    loadFile = []

for idx in range(1, len(argv)):
    loadFile.append(argv[idx])

save_to_json_file(loadFile, 'add_item.json')
