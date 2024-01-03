
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
    instr.append(0)


# clone the list so after trying to change each nop/jmp, it can reset to its original state
gi_clone = gi_split

# this next block of code loops through the instructions, increments the accumulator, and jumps
# when necessary. 
keep_going = True
instr_num = 0
accum = 0
swapped = 0

while keep_going:

    if instr_num > len(gi_split) - 1:
        print(f"\nthe value of the accumulator is {accum}")
        keep_going = False
        break

    active_instr = gi_split[instr_num]
    action = active_instr[0]
    num = active_instr[1]
    tally = active_instr[2]
    swap_tried = active_instr[3]

    if tally != 0:
        swapped = 0
        accum = 0
        instr_num = 0
        for instr in gi_split: # resets the 'tally' values to 0 for the next loop
            instr[2] = 0
    
    else:
        

        if action == 'acc':
            instr_num += 1
            active_instr[2] += 1
            accum += num
        
        if swapped == 1:
            if action == 'nop':
                instr_num += 1
                active_instr[2] += 1
            
            if action == 'jmp':
                instr_num += num
                active_instr[2] += 1
        
        else: # i.e. if swapped == 0
            if action == 'nop' and swap_tried == 1:
                instr_num += 1
                active_instr[2] += 1
            
            elif action == 'nop':
                swapped = 1
                active_instr[3] = 1 #sets swap_tried = 1 for this instruction
                instr_num += num
                active_instr[2] += 1
            
            if action == 'jmp' and swap_tried == 1:
                instr_num += num
                active_instr[2] += 1
            
            elif action == 'jmp':
                swapped = 1
                active_instr[3] = 1 #sets swap_tried = 1 for this instruction
                instr_num += 1
                active_instr[2] += 1
        



