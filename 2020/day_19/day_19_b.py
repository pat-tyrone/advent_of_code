import numpy as np

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
    """never called in this module"""
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

def rule_8_list(dict_of_rules, messages):
    initial_list = ok_words(dict_of_rules, 8)

    il_max_len = 0
    for il_i in initial_list:
        if len(il_i) > il_max_len:
            il_max_len = len(il_i)
    max_len = 0
    for msg in messages:
        if len(msg) > max_len:
            max_len = len(msg)

    trimmed_list = []
    for word in initial_list:
        keep_word = False
        for okw in messages:
            if word in okw:
                keep_word = True
                break
        if keep_word:
            trimmed_list.append(word)

    iters_needed = int((max_len - (max_len % il_max_len)) / il_max_len)
    #print(f" 8 iters_needed = {iters_needed}")

    return_list = []
    mult_list = ['']

    for i in range(iters_needed):
        for word in mult_list:
            #remove_from_mult_list = True
            for bb_word in trimmed_list:
                #print(f"bb_word = {bb_word}; bb_1 = {bb_1}; bb_2 = {bb_2}")
                test_word = word + bb_word
                for good_word in messages:
                    if test_word in good_word:
                        #print(f"test_word: {test_word}; in good_word: {good_word}")
                        return_list.append(test_word)
                        mult_list.append(test_word)
                        break
            mult_list.remove(word)



    #print(return_list)
    return return_list

def rule_11_list(dict_of_rules, messages):
    initial_list = ok_words(dict_of_rules, 11)

    il_max_len = 0
    for il_i in initial_list:
        if len(il_i) > il_max_len:
            il_max_len = len(il_i)
    #print(f"11 il_max_len = {il_max_len}")
    max_len = 0
    for msg in messages:
        if len(msg) > max_len:
            max_len = len(msg)

    trimmed_list = []
    for word in initial_list:
        keep_word = False
        for okw in messages:
            if word in okw:
                keep_word = True
                break
        if keep_word:
            trimmed_list.append(word)

    iters_needed = int((max_len - (max_len % il_max_len)) / il_max_len)
    #print(f" 11 iters_needed = {iters_needed}")

    return_list = []
    mult_list = ['']

    for i in range(iters_needed):
        for word in mult_list:
            #remove_from_mult_list = True
            for bb_word in trimmed_list:
                bb_1 = bb_word[:5]
                bb_2 = bb_word[5:]
                #print(f"bb_word = {bb_word}; bb_1 = {bb_1}; bb_2 = {bb_2}")
                test_word = bb_1 + word + bb_2
                for good_word in messages:
                    if test_word in good_word:
                        #print(f"test_word: {test_word}; in good_word: {good_word}")
                        return_list.append(test_word)
                        mult_list.append(test_word)
                        break
            mult_list.remove(word)
    return return_list

def ok_words_2(dict_of_rules, rule_num):
    """creates a list of strings, with each being an acceptable value based on the specified rule
    no rule argument will (eventually) return a full list of acceptable words"""

    func_dict = dict_of_rules
    func_dict['8'] = rule_8_list(dict_of_rules, '8', msgs)
    func_dict['11'] = rule_8_list(dict_of_rules, '11', msgs)

    #print(func_dict)

    start_list = func_dict[str(rule_num)]

    rule_list = []
    for item in start_list:
        print(item)
        try:
            rule = ok_words_2(func_dict, item)
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

    #print(working_list)
    return working_list


def solve_p1(messages, dict_of_rules, rule_num_to_match):
    
    acceptable_msgs = ok_words(dict_of_rules, rule_num_to_match)
    
    matches = []

    for msg in messages:
        if msg in acceptable_msgs:
            matches.append(msg)
    
    return len(matches)

def solve_p2(messages, dict_of_rules, rule_num_to_match):

    r8 = rule_8_list(dict_of_rules, messages)
    r11 = rule_11_list(dict_of_rules, messages)

    mult_list = [r8, r11]
    
    acceptable_msgs = multiply_lists(mult_list)

    #print(len(r8))
    #print(r8)
    #print(len(r11))
    #print(r11)
    #print(len(acceptable_msgs))
    
    matches = []

    for msg in messages:
        if msg in acceptable_msgs:
            matches.append(msg)
    
    return len(matches)


#print(ok_words(rules_dict,42))
#print(rule_8_list(rules_dict, 8, msgs))

print(solve_p2(msgs, rules_dict, 0))

