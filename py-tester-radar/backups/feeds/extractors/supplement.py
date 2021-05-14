# encoding: utf-8
import json
from typing import Callable

import yaml


class __Sentinel:
    """
    singleton base class
    """

    def __repr__(self):
        return "sentinel"


sentinel = __Sentinel()


class TRStr:

    def __init__(self, func: Callable):
        self.func = func

    def __str__(self):
        return self.func()


def yml_to_json(yaml_path: str) -> str:
    with open(yaml_path, 'r') as data:
        dict_data = yaml.load(data)
    return to_json(dict_data)


def yml_to_dict(yaml_path: str) -> str:
    with open(yaml_path, 'r') as data:
        dict_data = yaml.load(data)
    return dict_data


def to_json(dict_value: dict):
    return json.dumps(dict_value, sort_keys=True)


def load_json_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as f:
            json_dict = json.load(f, encoding='utf-8')
    except FileNotFoundError as e:
        print(e)
        return dict()
    return json_dict


def write_to_json_file(dict_values: any, file_path: str):
    with open(file_path, 'w') as f:
        json.dump(dict_values, f)


__all__ = ("TRStr", "sentinel")
