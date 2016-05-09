''' Goals: Make tests reusable with parameters and functions



'''

import topology
import parsers
import aetest

from pprint import pprint

def dialin():
    tb = topology.load('notes/sim_test.yaml')
    dev = tb.devices['pyats-asa-2']
    dev.connect()
    dev.config('''
        interface GigabitEthernet0/0
        nameif inside
        serity-level 100
        ip address 10.0.0.1 255.255.255.0
        no shut
    ''')
    return dev

def restore(dev):
        dev.config('''
        clear config object
        clear config access-group
        clear config interface g0/0
        ''')
        dev.disconnect()
    
    
class PingTests(aetest.Testcase):
    def test_no_ping_packets_lost(self):
        'Verify that a ping had 0% packet loss'

        dev = dialin()
        ############## Ping Tests ###########################################
        # Test objective: Verify that no packet are lost:  ping www.cisco.com
        output = dev.execute('ping www.cisco.com')
        ping_result = parsers.parse_ping(output)
        assert ping_result.loss_rate == 0.0

        restore(dev)
    test_no_ping_packets_lost.test = True

##### IPV4 Interface Tests  #########################################
class IPV4_Interface_Tests():
    def verify_minimum_ipv4_interfaces_up():
        'verify that at least 5 interfaces have an "Up" status'
        dev = dialin()
        output = dev.execute('show ipv4 int bri')
        interfaces = parsers.parse_interfaces(output)

        # Test objective 1: "show ipv4 int bri" and verify that at least 5 interfaces have an "Up" status
        # assert len([iface[0] for iface in interfaces if iface[2] == 'Up']) >= 5
        assert sum([iface.status == 'up' for iface in interfaces]) >= 5

        restore(dev)
    verify_minimum_ipv4_interfaces_up.test = True


def verify_not_too_many_ipv4_up_interfaces_unassigned():
    'Verify if more unassigned interfaces'
    dev = dialin()
    output = dev.execute('show ipv4 int bri')
    interfaces = parsers.parse_interfaces(output)

    assert sum([iface.ipaddr == 'unsassigned'
                    for iface in interfaces
                    if iface.status == 'up']) <= 6

    restore(dev)
   

if __name__ == '__main__':

    testcases = [PingTests(),IPV4_Interface_Tests()]
    aetest.run_test(testcases)
    
    #tests = [ test_no_ping_packets_lost, verify_minimum_ipv4_interfaces_up]
    #aetest.run_test(tests)


    
