

epd = 0
buses = []
notes = []

with open('input') as input_file:
    for line in input_file:
        notes.append(line.rstrip())

epd = int(notes[0])
buses = notes[1].split(',')

for i in range(len(buses)):
    bus_i = buses.pop(0)
    if bus_i.lower() != 'x':
        buses.append(int(bus_i))

next_deps = []

for bus in buses:
    nd = 0
    while nd < epd:
        nd += bus
    next_deps.append(nd)

my_dep = min(next_deps)

my_bus_index = next_deps.index(my_dep)
my_bus = buses[my_bus_index]

my_wait = my_dep - epd

ans = my_bus * my_wait

print(ans)