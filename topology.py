'Model, in miniature, the functions of ats.topology'

import yaml
from pprint import pprint
from keyedlist import KeyedList
import sys


class Device:
    def __init__(self, devname, **kwargs):
        self.devname = devname
        self.__dict__.update(kwargs)
    def connect(self):
        pass
    def disconnect(self):
        pass
    def config(self):
        pass
    def execute(self):
        pass


from sim import Device    # <== Overwrite the stub device with the simulator

def load(filename):
    '''load a topology file.
       Return a testbed object'''
    #1 Read the YAML file
    # Potential problem: Invalid YAML
    # Solution: Use try_yaml.py to figure-out the problem
    #           or just nudge it to become more JSON-like
    with open(filename) as f:
        tb = yaml.load(f)

    #2 Wrap the multi-level dict in a keyed list
    #  Purpose make lookups simpler using dots instead of square bracket
    tb = KeyedList(tb)

    #3 Schema validation -- Even if the YAML is valid, the keys might be misspelled
    #  Potential problem: Unexpected keys
    #  Solution: Fix the spelling of that key
    toplevel_schema = {'testbed', 'devices', 'topology'}
    if not set(tb).issubset(toplevel_schema):
        print('Bad top level keys: %r' % str(set(tb) - toplevel_schema))
        sys.exit(1)

    #4 Replace some dictionary entries with classes
    for devname, devvalue in tb.devices.items():
        tb.devices[devname] = Device(devname, **devvalue)

    return tb

if __name__ == '__main__':
    tb = load('notes/sim_test.yaml')
    pprint(tb)

