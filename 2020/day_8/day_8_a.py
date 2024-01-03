
gi_raw = []

with open('input') as input_file:
    for line in input_file:
        gi_raw.append(line.rstrip())

# an empy list to hold the instructions as a list of lists
gi_split = []

# these two for loops split the instructions into action/number, and then convert the number to an integer
# it also adds a third element to each sub list and sets it equal to 0. This will be used to detect
# repeated instructions
for instr in gi_raw:
    instr = instr.split(' ')
    gi_split.append(instr)

for instr in gi_split:
    instr[1] = int(instr[1])
    instr.append(0)


# this next block of code loops through the instructions, increments the accumulator, and jumps
# when necessary. 
no_dupes = True
instr_num = 0
accum = 0

while no_dupes:
    active_instr = gi_split[instr_num]
    action = active_instr[0]
    num = active_instr[1]
    tally = active_instr[2]

    if tally != 0:
        no_dupes = False
        break

    if action == 'nop':
        instr_num += 1
        active_instr[2] += 1

    if action == 'acc':
        instr_num += 1
        active_instr[2] += 1
        accum += num
    
    if action == 'jmp':
        instr_num += num
        active_instr[2] += 1
    
print(f"\nthe value of the accumulator when instructions first repeat is {accum}")









# for i in gi_split:
#     if i[0] == 'nop' and i[1] != 0:
#         print(i)


