
puzz_in = []

with open("data.txt") as f:
    for line in f:
        puzz_in.append(line.rstrip())

# Part 1

def bi_to_dec(x_in):
    if type(x_in) == str:
        x = list(x_in)
    else:
        x = x_in
    binary_num = 0
    exp = 0
    for i in range(len(x)):
        dig = int(x.pop())
        subtotal = (2**exp) * dig
        binary_num += subtotal
        exp += 1
    
    return binary_num


def calc_gamma(list_in):
    bit_list = []
    for item in list_in:
        item_split = list(item)
        bits = []
        for bit in item_split:
            bits.append(int(bit))
        bit_list.append(bits)
    
    gamma_list = []
    numer = 0
    denom = 0

    for i in range(len(bit_list[0])):
        for item in bit_list:
            numer += item[i]
            denom += 1

        if numer/denom < 0.5:
            gamma_list.append(0)
        else:
            gamma_list.append(1)
        
        numer = 0
        denom = 0
    
    return(gamma_list)


def calc_epsilon(list_in):
    bit_list = []
    for item in list_in:
        item_split = list(item)
        bits = []
        for bit in item_split:
            bits.append(int(bit))
        bit_list.append(bits)
    
    ep_list = []
    numer = 0
    denom = 0

    for i in range(len(bit_list[0])):
        for item in bit_list:
            numer += item[i]
            denom += 1

        if numer/denom >= 0.5:
            ep_list.append(0)
        else:
            ep_list.append(1)
        
        numer = 0
        denom = 0
    
    return(ep_list)
            

def find_oxy(list_in):
    possibles = [a for a in list_in]
    bin_len = len(possibles[0])
    counter = 0
    
    while True:
        if len(possibles) == 1:
            return possibles[0]
            break

        target_bin = calc_gamma(possibles)
        
        bit_pos = counter % bin_len
        bit_crit = target_bin[bit_pos]
        to_be_removed = []

        for item in possibles:
            bit_tested = int(item[bit_pos])
            if bit_tested != bit_crit:
                to_be_removed.append(item)

        for removal in to_be_removed:
            possibles.remove(removal)
            if len(possibles) == 1:
                break

        
        counter += 1


def find_co2(list_in):
    possibles = [a for a in list_in]
    bin_len = len(possibles[0])
    counter = 0
    
    while True:
        if len(possibles) == 1:
            return possibles[0]
            break

        target_bin = calc_epsilon(possibles)
        
        bit_pos = counter % bin_len
        bit_crit = target_bin[bit_pos]
        to_be_removed = []

        for item in possibles:
            bit_tested = int(item[bit_pos])
            if bit_tested != bit_crit:
                to_be_removed.append(item)

        for removal in to_be_removed:
            possibles.remove(removal)
            if len(possibles) == 1:
                break

        
        counter += 1


part_1_sol = bi_to_dec(calc_gamma(puzz_in)) * bi_to_dec(calc_epsilon(puzz_in))
print(f"\n\tPart 1 solution: {part_1_sol}")

part_2_sol = bi_to_dec(find_oxy(puzz_in)) * bi_to_dec(find_co2(puzz_in))
print(f"\n\tPart 2 solution: {part_2_sol}")
