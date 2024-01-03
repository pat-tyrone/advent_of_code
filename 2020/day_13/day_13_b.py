from math import gcd

def lcm(a,b):
    return a*b // gcd(a,b)

epd = 0
buses = []
notes = []

with open('input') as input_file:
    for line in input_file:
        notes.append(line.rstrip())

epd = int(notes[0])
buses = notes[1].split(',')

def_buses = []

for i in range(len(buses)):
    bus_i = buses.pop(0)
    if bus_i.lower() != 'x':
        buses.append(int(bus_i))
        def_buses.append(int(bus_i))
    else: buses.append(bus_i)

slow_bus = max(def_buses)

t_offsets = {}

for bus in def_buses:
    t_offset = buses.index(bus) - buses.index(slow_bus)
    t_offsets[bus] = t_offset




t_test = 0

#print(t_offsets)





epd = slow_bus
increment = slow_bus

for bus in def_buses:

    if bus != slow_bus:
        
        while True:

            if (epd + t_offsets[bus]) % bus != 0:
                epd += increment
            else:
                increment = lcm(increment, bus)
                break

    if bus == def_buses[-1]:
        print(f"EPD = {epd + t_offsets[def_buses[0]]}")

