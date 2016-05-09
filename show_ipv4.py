'Learn to parse the column-oriented text typical of output from the Cisco IOS'
# Goal: Show neatly formatted output with the ipaddr and interface with the status up.

#1 Acquire data
with open('notes/ipv4_int_bri.txt') as f:
    output = f.read()          # dev.execute('show ipv4 int bri')

#2 parse data and convert into convenient format
ifaces = []
for line in output.splitlines():
    #interface, ipaddr, status, protocol = line.split()
    interface = line[0:31].rstrip()
    ipaddr = line[31:47].rstrip()
    status = line[47:69].rstrip()
    protocol = line[69:].rstrip()
    ifaces.append((interface, ipaddr, status, protocol))
    

#3 data analysis/test/formatted data    
#    if status == 'Up':
#        print('%-16s %s' % (ipaddr, interface))

for iface in ifaces:
    if iface[2] == 'Up':
        print('%-16s %s' % (iface[1], iface[0]))


