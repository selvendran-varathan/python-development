'Model, in miniature, the function of ats.topology'


import yaml
from pprint import pprint
from keyedlist import KeyedList
import sys

class Device:
    pass
    
def load():
    'Load a topology file'
    with open('notes/sim_test.yaml') as f:
          tb = yaml.load(f)


    tb = KeyedList(tb)

    toplevel_schema = {'testbed','devices','topology'}

    pprint('start')
    pprint(tb)

    if not set(tb.keys()).issubset(toplevel_schema):
        print('Bad top level keys: %r' % str((set(tb.keys()) - toplevel_schema)))
        sys.exit(1)

    for devname, devvalue in tb.devices.items():
       tb.devices[devname] = Device(devname, **devvalue)

    return tb

    if __name__ == '__main__':
        tb=load('notes/sim_test.yaml')
        pprint(tb)
