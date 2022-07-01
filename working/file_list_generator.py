#!/usr/bin/env python3

import json
import os
from re import M

f = open("./config.json")
config = json.load(f)
f.close()
all_files = config['all_files']

def init_file_list():
    return os.listdir(all_files)

def init_jpg_list(lst):
    jpg_files = [f for f in lst if f.endswith(('.jpg', '.jpeg'))]
    return jpg_files

def init_mp4_list(lst):
    mp4_files = [f for f in lst if f.endswith('.mp4')]
    return mp4_files
