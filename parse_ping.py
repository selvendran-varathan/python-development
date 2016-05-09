'Test objective: Verify there is no packet loss'

from parsers import parse_ping

#1 Acquire data
with open('notes/ping_output.txt') as f:
    output = f.read()

#2 Parsing data and convert it to a convenient form
transmitted, received, loss_rate = parse_ping(output)

#3 Data analysis/tests/formatted output
assert loss_rate == 0.0
