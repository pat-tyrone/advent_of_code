def construct_mul(string, x_str='', y_str='', comma_bool=False):
    """returns tuple of multiplicands. If invalid args are passed, returns (0,0)"""

    if (len(string) > 0):
        s = string[1:]
        x = x_str
        y = y_str
        fc = string[0]
    else:
        return(0,0)

    if (fc == ')') and (len(x)>0) and (len(y)>0):
        if (len(x)>3) or (len(y)>3):
            print(f"x = {x}; y = {y}")
        return (int(x), int(y))
    elif fc == ')':
        return (0,0)
    elif (fc == ',') and (len(x)>0) and (not comma_bool):
        return construct_mul(s, x, '', True)
    elif (fc == ','):
        return (0,0)  
    elif (fc.isdigit()) and (not comma_bool):
        new_x = x + fc
        return construct_mul(s, new_x, '', False)
    elif (fc.isdigit()) and (comma_bool):
        new_y = y + fc
        return construct_mul(s, x, new_y, True)
    elif not fc.isdigit():
        return (0,0)
    else:
        print("THERE WAS AN ERROR")
        return (0,0)


file = 'input.txt'
mem_lines = []
with open(file) as f:
    for line in f:
        mem_lines.append(line)

# solves p1
p1_ans = 0
for line in mem_lines:
    parts = line.split('mul(')
    for part in parts:
        mult_tup = construct_mul(part)
        p1_ans += (mult_tup[0] * mult_tup[1])

# solves p2
do = True
do_strings = []
for line in mem_lines:
    dn_split = line.split("don't()")
    if do:
        dn_split[0] = "do()" + dn_split[0]
    
    for item in dn_split:
        try:
            do_idx = item.index("do()")
            do_strings.append(item[do_idx:])
        except:
            pass
    
    # sets the 'do' Boolean for the start of the next line in mem_lines[]
    if "do()" not in dn_split[-1]:
        do = False
    else:
        do = True

p2_ans = 0
for ds in do_strings:
    parts = ds.split('mul(')
    for part in parts:
        mult_tup = construct_mul(part)
        p2_ans += (mult_tup[0] * mult_tup[1])

print(f"p1 ans: {p1_ans}")
print(f"p2 ans: {p2_ans}")