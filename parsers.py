'Collection of rehusable parsing utilities'

import re

from collections import namedtuple
PingResult = namedtuple('PingResult', ['transmitted', 'received', 'loss_rate'])
Interface = namedtuple('Interface', ['interface', 'ipaddr', 'status', 'protocol'])

class NoMatch(KeyError):
    'Exception raised when an expected pattern is not found'


def parse_ping(output):
    'Parse the output of a ``ping`` in to a tuple'
    ping_result_pattern = r'^(\d+) packets transmitted, (\d+) packets received, ([\d.]+)% packet loss'
    mo = re.search(ping_result_pattern, output, flags=re.MULTILINE)
    if mo is None:
        raise NoMatch(ping_result_pattern, output)
    transmitted, received, loss_rate = mo.groups()

    return PingResult(int(transmitted), int(received), float(loss_rate))



def parse_interfaces(output):
    '''Parse the output of ``show ipv4 interfaces brief``.
       Return a list of tuples in the form [(interface, ipaddr, status, protocol), ...]
    '''
    ifaces = []
    for line in output.splitlines():
        interface = line[0:31].rstrip()
        ipaddr = line[31:47].rstrip()
        status = line[47:69].rstrip().lower()
        protocol = line[69:].rstrip().lower()
        iface = Interface(interface, ipaddr, status, protocol)
        ifaces.append(iface)
    return ifaces