def is_val_in_range(val_, range_):
    """returns T/F depending on whether value is within a range
    range arg is given as a list: [min, max]"""
    if val_ >= range_[0] and val_ <= range_[1]:
        return True
    else:
        return False

def is_val_in_either_range(val_, range_pair):
    """returns T/F depending on whether value is within either range in a range pair
    range_pair arg is given as a list with two sublists: [[min, max],[min, max]]"""

    if is_val_in_range(val_, range_pair[0]):
        return True
    elif is_val_in_range(val_, range_pair[1]):
        return True
    else:
        return False

def is_val_in_any_range(val_, range_list):
    """like is_val)in_either_range, but takes a list of ranges of any lenth as the second arg"""
    result = False
    for rng in range_list:
        if is_val_in_range(val_, rng):
            result = True
            break
    return result

def convert_range_to_ints(rng_str):
    """converts a range string 'min-max' to a two item list of ints [int(min), int(max)]"""
    split = rng_str.split('-')
    range_min = int(split[0])
    range_max = int(split[1])
    min_max = [range_min, range_max]
    return min_max

def calc_tser(ticket_list, range_list):
    """returns the answer for part 1. ticket list must be formatted so each ticket is a list of integers
    and tange list must be a list of sublists, with each sublist a two item list: [min,max].
    Min and max must also be integers"""
    tser = 0
    for bt in ticket_list:
        for num in bt:
            if is_val_in_any_range(num, range_list):
                continue
            else:
                tser += num
    return tser


# empty list to hold the initial import of rules as a text string to be parsed
rules = []

# this is a list of lists, with each sublist representing a single ticket as a list of integers
nb_tix = []

# my ticket will be a simple list of integers
my_ticket = []

with open('rules.txt') as the_rules:
    for line in the_rules:
        rules.append(line.strip())

with open('nearby_tix.txt') as tix:
    for tick in tix:
        nb_tix.append(tick.strip())

with open('my_ticket.txt') as mt:
    for field in mt:
        my_ticket.append(field.strip())

# convert my ticket into a list of integers
fix_ticket = my_ticket.pop()
fix_ticket = fix_ticket.split(',')
for field in fix_ticket:
    my_ticket.append(int(field))




tick_fields = [] # will hold the field names
rules_fr = [] # list of the first ranges in each rule's range pair
rules_sr = [] # list of the second ranges in each rule's range pair

# a list of both rules in each rule's range pair. Each item has TWO ranges for ONE rule.
# each item can be fed as the second arg for is_val_in_either_range()
rules_br = []

# will hold all ALL ranges for dumb checks like "is this number valid anywhere?"
all_ranges = []

for rule in rules:
    split_field = rule.split(': ')
    tick_fields.append(split_field[0]) # adds the field name to tick_fields[]

    split_or = split_field[1].split(' or ') # split the first and second range for each rule
    fr = convert_range_to_ints(split_or[0]) # fr becomes a two item list of integers: [min_0, max_0]
    sr = convert_range_to_ints(split_or[1]) # sr becomes a two item list of integers: [min_1, max_1]

    # append each range to its proper list
    rules_fr.append(fr)
    rules_sr.append(sr)

    for_br = [] # create a two-item list for each rule's range_pair: [[min_0, max_0], [min_1, max_1]]
    for_br.append(fr)
    for_br.append(sr)
    rules_br.append(for_br) # add the range pair to rules_br[]

    # add fr ans sr to the dumb list all_ranges[]
    all_ranges.append(fr) 
    all_ranges.append(sr)




# this block of code populates nb_tix with ALL tickets (except mine)
for tick in range(len(nb_tix)):
    pop = nb_tix.pop(0)
    fields = pop.split(',')
    field_ints = []
    for field in fields:
        field_ints.append(int(field))
    nb_tix.append(field_ints)


bad_tix = []
good_tix = []

# this loops through nb_tix and tests each ticket by seeing if it has any universally invalid values
# it moves those with bad values to bad_tix, and those passing the test to good_tix.
# nb_tix is empty when the loop finishes.
while nb_tix:
    
    test_ticket = nb_tix.pop(0)
    good_tick = True

    for num in test_ticket:
        if is_val_in_any_range(num, all_ranges):
            continue
        else:
            good_tick = False
            break

    if good_tick:
        good_tix.append(test_ticket)
    else:
        bad_tix.append(test_ticket)


# need to create a list for each ticket field. For example, values_f1 will be a list of each of the 
# field 1 values across all (good) tickets
num_fields = len(good_tix[0]) 
field_values_dict = {}
for value in range(num_fields):
    val_list = []
    for tick in good_tix:
        val_list.append(tick[value])
    field_values_dict[value] = val_list

field_rules_dict = {}
for value in range(len(fields)):
    rule_name = tick_fields[value]
    nums_allowed = rules_br[value]
    field_rules_dict[rule_name] = nums_allowed


# this is where we begin to test field values to dtermine mappings
confirmed_mappings = {}

keep_going = True
while keep_going:

    poss_mappings = {}

    for tf in field_values_dict.keys(): #tf is the key, which is a field number in this dict
        test_values = field_values_dict[tf]

        for field in field_rules_dict.keys():
            allowed_nums = field_rules_dict[field] # allowed_nums is a range pair [[min_0,max_0], [min_1,max_1]]
            mapping_possible = True
            for tv in test_values:
                
                if is_val_in_any_range(tv, allowed_nums):
                    continue
                else:
                    mapping_possible = False
                    break

            if mapping_possible:
                if field in poss_mappings.keys():
                    poss_mappings[field].append(tf)
                else:
                    new_poss_mapping = []
                    new_poss_mapping.append(tf)
                    poss_mappings[field] = new_poss_mapping

    transfer_field = {}
    for k, v in poss_mappings.items():
        if len(v) == 1:
            transfer_field[k] = v[0]

    for k,v in transfer_field.items():
        confirmed_mappings[k] = v
        #del poss_mappings[k] # prob don't need this one I implement while loop
        del field_values_dict[v]
        del field_rules_dict[k]

    if len(field_values_dict.keys()) < 1:
        keep_going = False


my_ticket_dict = {}

for field_name in tick_fields:
    field_num = confirmed_mappings[field_name]
    field_value = my_ticket[field_num]
    my_ticket_dict[field_name] = field_value

p2_ans = 1

for field_name in my_ticket_dict.keys():
    if 'departure' in field_name.lower():
        p2_ans = p2_ans * my_ticket_dict[field_name]

print(f"p2_ans = {p2_ans}")



            