#!/usr/bin/python3
"""define add item"""
import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
args = load_from_json_file("add_item.json")
args += sys.argv[1:]
save_to_json_file(args, "add_item.json")
