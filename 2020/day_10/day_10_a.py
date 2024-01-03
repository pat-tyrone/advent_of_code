jas = []

with open('input') as input_file:
    for line in input_file:
        jas.append(int(line.rstrip()))

# sort the list, so it is in the order that each joltage adapter is connected
jas.sort()

# insert a 0 entry for the wall, and max+3 for my device, per the rules
jas.insert(0, 0)
jas.append(max(jas)+3)

# empty list to hold the joltage differences
ja_diffs = []

# iterate through the list and store the diffs b/w each adapter
for value in range(1, len(jas)):
    diff = jas[value] - jas[value -1]
    ja_diffs.append(diff)

# the answer is the number of 1 jolt diffs times the number of 3 jolt diffs
print(f"there are {ja_diffs.count(1)} 1-jolt diffs, and {ja_diffs.count(3)} 3-jolt diffs. \
so the answer is {ja_diffs.count(1)} x {ja_diffs.count(3)} = {ja_diffs.count(1)*ja_diffs.count(3)}.")