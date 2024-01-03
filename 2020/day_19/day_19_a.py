
rules_msgs = []

with open('input.txt') as in_19:
    for line in in_19:
        rules_msgs.append(line.rstrip())

rules = []
msgs = []

switch_to_msgs = False
for line in rules_msgs:
    if switch_to_msgs == False:
        if line == '':
            switch_to_msgs = True
        else:
            rules.append(line)
    else:
        msgs.append(line)

for i in range(len(rules)):
    split = rules.pop(0).split(': ')
    rule_index = split[0]
    rule_instr = split[1]
    if 'a' in rule_instr or 'b' in rule_instr:
        rule_instr = list(rule_instr.replace('"', ''))
    else:
        rule_instr = split[1].split(' ')


    new_rule = [rule_index, rule_instr]
    rules.append(new_rule)

rules_dict = {}

for rule in rules:
    rules_dict[rule[0]] = rule[1]

# print(rules_dict)

def split_or_instr(list_w_bar):
    return_list = []
    list_builder = []
    for i in list_w_bar:
        if i != '|':
            list_builder.append(i)
        else:
            return_list.append(list_builder)
            list_builder = []
    return_list.append(list_builder)
    return return_list


def remove_sublists(my_list):
    """converts a list which may have sublists into a list of single elements"""
    working_list = my_list
    keep_going = True
    while keep_going:
        keep_going = False
        for item in working_list:
            if isinstance(item, list):
                keep_going = True
                while item:
                    popout = item.pop(0)
                    working_list.insert(working_list.index(item), popout)
                working_list.remove(item)
    return working_list

def add_lists(list_of_lists):
    working_list = []
    for sublist in list_of_lists:
        if isinstance(sublist, list):
            for item in sublist:
                working_list.append(item)
        else:
            working_list.append(sublist)
    
    return working_list

def multiply_lists(list_of_lists):
    working_list = ['']
    for sublist in list_of_lists:
        if isinstance(sublist, str):
            for i in range(len(working_list)):
                wl_pop = working_list.pop(0)
                new_str = wl_pop + sublist
                working_list.append(new_str)
        elif isinstance(sublist, list):
            for i in range(len(working_list)):
                wl_pop = working_list.pop(0)
                for j in sublist:
                    new_str = wl_pop + j
                    working_list.append(new_str)
                    
    
    return working_list
                


def ok_words(dict_of_rules, rule_num):
    """creates a list of strings, with each being an acceptable value based on the specified rule
    no rule argument will (eventually) return a full list of acceptable words"""

    return_list = ['']

    start_list = dict_of_rules[str(rule_num)]

    rule_list = []
    for item in start_list:
        try:
            rule = ok_words(dict_of_rules, item)
            rule_list.append(rule)
        except:
            rule_list.append(item)
    
    if '|' in rule_list:
        working_list = []
        or_list = split_or_instr(rule_list)
        for alt in or_list:
            to_wl = multiply_lists(alt)
            working_list.append(to_wl)
        working_list = add_lists(working_list)
    
    else:
        working_list = multiply_lists(rule_list)

    return working_list

def solve_p1(messages, dict_of_rules, rule_num_to_match):
    
    acceptable_msgs = ok_words(dict_of_rules, rule_num_to_match)
    
    matches = []

    for msg in messages:
        if msg in acceptable_msgs:
            matches.append(msg)
    
    return len(matches)

def solve_p2(messages, dict_of_rules, rule_num_to_match):
    
    acceptable_msgs = ok_words(dict_of_rules, rule_num_to_match)
    
    matches = []

    for msg in messages:
        if msg in acceptable_msgs:
            matches.append(msg)
    
    for msg in acceptable_msgs:
        print(msg)

print(solve_p2(msgs, rules_dict, 42))


