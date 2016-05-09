import topology
import parsers
import aetest


from pprint import pprint

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

############## Ping Tests ###########################################
# Test objective: Verify that no packet are lost:  ping www.cisco.com
output = dev.execute('ping www.cisco.com')
ping_result = parsers.parse_ping(output)
assert ping_result.lost_rate == 0.0


##### IPV4 Interface Tests  #########################################
output = dev.execute('show ipv4 int bri')
interfaces = parsers.parse_interfaces(output)

# Test objective 1: "show ipv4 int bri" and verify that at least 5 interfaces have an "Up" status
