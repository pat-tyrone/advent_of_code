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

            x_chars = mask.count('X')
            variations = 2 ** x_chars

            bin_vars = []
            for value in range(variations):
                bin_vars.append(bin(value)[2:].zfill(x_chars))
            
            

        # assign value to proper address in mem{} if this is a mem command
        elif result.group() == 'mem':
            address = int(re.search(r'\d+', command).group())

            value = int(re.search(r'\d+$', command).group())
            bin_address = bin(address)[2:].zfill(36)


            address_masked = ''

            for char in range(36):
                if mask[char] == 'X':
                    address_masked = address_masked + 'X'
                elif mask[char] == '1':
                    address_masked = address_masked + '1'
                else:
                    address_masked = address_masked + bin_address[char]
            


            for var in range(variations):

                bin_var = list(bin_vars[var]) # binary representation of the variation number
                
                new_address = address_masked
                while bin_var:
                    sub_char = bin_var.pop(0)

                    new_address = re.sub('X', sub_char, new_address, 1)
            

                mem[new_address] = value


    # in order to anser the question, the values in mem{} must be a list so it is subscriptable
    values = list(mem.values())
    
    ans = 0

    # iterare through values and get a sum
    for value in values:
        ans += value

    print(f"ans = {ans}")


exec_ip(init_prog)

