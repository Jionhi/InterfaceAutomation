# coding=utf-8

import json
import os
import sys

base_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_path)
sys.path.append(parent_dir)


def read_json(file_name):
    if file_name is None:
        file_name = parent_dir + '/config/user_data.json'
    else:
        file_name = parent_dir + file_name
    with open(file_name, encoding='utf-8') as fp:
        data = json.load(fp)
    return data


def get_value(key, file_name=None):
    data = read_json(file_name)
    # return data[key]
    return data.get(key)