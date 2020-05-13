from addict import Dict

from util.file_reading import open_yaml

filename = "endpoints.yaml"


def endpoint():
    yaml = open_yaml(filename)
    return Dict(yaml)