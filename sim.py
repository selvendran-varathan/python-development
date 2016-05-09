''' Simulate a device object '''

import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Device:

    def __init__(self, devname, connections, **kwargs):
        self.devname = devname
        self.connections = connections
        self.__dict__.update(kwargs)

    def execute(self, command):
        '''In the real ATS system, this sends a command to a device and returns
           a string with result.  We are going to simulate execution with
           pre-recorded results.

        '''
        if 'ping' in command:
            filename = 'notes/ping_output.txt'
        elif 'info' in command:
            filename = 'notes/show_info_output.txt'
        elif 'version' in command:
            filename = 'notes/show_version_output.txt'
        elif 'ipv4' in command:
            filename = 'notes/ipv4_int_bri.txt'
        elif 'xml' in command:
            filename = 'notes/interfaces.xml'
        else:
            raise ValueError('Unknown command: %r', command)
        LOGGER.info('Executing command: %r' % command)
        with open(filename) as f:
            output = f.read()
        if 'ping' in command:
            output = output.replace('www.cisco.com', command.split()[-1])
        LOGGER.info('Device replied with:\n%s' % output)
        return output

    def config(self, string_of_config_commands):
        'Simulate the real PyATS feature than can run a whole series config lines all at once'
        LOGGER.info('Configuring %r with:\n%s', self.devname, string_of_config_commands)

    def connect(self, via='a', alias=None):
        'Simulate a call that connects'
        conn = self.connections[via]
        if 'port' in conn:
            LOGGER.info('Connecting to %r using %s on %s port %s',
                         self.devname, conn.protocol, conn.ip, conn.port)
        else:
            LOGGER.info('Connecting to %r using %s on %s',
                         self.devname,conn.protocol, conn.ip)

    def disconnect(self):
        'Simulate a call that disconnects'
        LOGGER.info('Disconnecting from %r', self.devname)

if __name__ == '__main__':

    class AttrDict(dict):
        def __init__(self, **kwds):
            self.__dict__ = self
            self.update(kwds)

    connections = AttrDict(
        a =   AttrDict(protocol='telnet', ip='10.85.84.80', port=2001),
        b =   AttrDict(protocol='telnet', ip='10.85.84.80', port=2003),
        alt = AttrDict(protocol='telnet', ip='5.19.27.5'),
    )

    asa = Device('ott-tb1-n7k4', connections=connections)
    asa.connect(via='alt')
    asa.connect()
    asa.config('''
          interface GigabitEthernet0/0
            nameif inside
            security-level 100
            ip address 10.0.0.1 255.255.255.0
            no shut
    ''')
    output = asa.execute('ping www.wikipedia.org')
    asa.disconnect()

