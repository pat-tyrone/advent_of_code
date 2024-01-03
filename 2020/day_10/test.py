
jas = []


with open('input') as input_file:
    for line in input_file:
        jas.append(int(line.rstrip()))

# sort the list, so it is in the order that each joltage adapter is connected
jas.sort()

for value in range(10):
    print(jas[value])

print(len(jas))