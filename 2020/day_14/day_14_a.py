import re

# empty list to hold commands in the initialization program
init_prog = []

# populate init_prog
with open('input', 'r') as file_input:
    for line in file_input:
        init_prog.append(line.rstrip())


def exec_ip(commands):
    """function to get the answer to part 1"""
    
    #empty dictionary to hold address:value pairs
    mem = {}

    # variable to hold mask values
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    
    for command in commands:

        # regex to recognize if command is a mask or mem command
        # 'result' will be wither 'mask' or 'mem'
        pattern = re.compile('^[a-zA-Z]+')
        result = pattern.match(command)

        # update mask value if this is a mask command
        if result.group() == 'mask':
            mask = command[-36:]

        # assign value to proper address in mem{} if this is a mem command
        elif result.group() == 'mem':
            address = int(re.search(r'\d+', command).group())
            value = int(re.search(r'\d+$', command).group())
            bin_val = bin(value)[2:].zfill(36)

        
            bin_val_mask = ''

            for char in range(36):
                if mask[char] != 'X':
                    bin_val_mask = bin_val_mask + mask[char]
                else:
                    bin_val_mask = bin_val_mask + bin_val[char]
            
            mem[address] = bin_val_mask

    # in order to anser the question, the values in mem{} must be a list so it is subscriptable
    values = list(mem.values())
    
    ans = 0

    # iterare through values and get a sum
    for value in values:
        test_val = int(value, 2)
        ans += test_val

    print(f"ans = {ans}")


exec_ip(init_prog)

