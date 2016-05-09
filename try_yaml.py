'Tool for exploring and playing with YAML to learn how it works'


import yaml
from pprint import pprint

with open('yaml_test.yaml') as f:
    data=yaml.load(f)

pprint(data)
