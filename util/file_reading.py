import json

import yaml


def open_yaml(file):
    with open(file, 'r') as f:
        return yaml.load(f)


def open_json(file, schema=True):
    if schema:
        file = "schema/" + file
    with open(file) as json_file:
        return json.load(json_file)
