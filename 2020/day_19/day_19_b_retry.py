# the steps in this block all serve to read the input, and generate two lists:
# 1) rules_dict is a mapping of rules, which ultimately get stored in a dict like this:
# key: rule number as a string; value: list of strings, including references to other rules, and bar separators
# example: {'105': ['12', '|', '69'], '42': ['69', '48', '|', '12', '41']}
# 2) the 'msgs' list simply holds the messages in the input
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

# the purpose of the next two functions is to check for wubstring matches. Specifically, they get called
# at various times in the program to reduce the size of lists being compared, or "multiplied",
# to make the program run more efficiently
def is_str_in_words(str_list, word_list):
    """this function takes two lists as args. It checks the strings in str_list to see if they
    are a substring to any of the strings in word_list. It returns a list of strings that find a match"""
    keep_list = []
    for s in str_list:
        in_word = False
        for w in word_list:
            if s in w:
                in_word = True
                break
        if in_word:
            keep_list.append(s)
    return keep_list

def does_word_contain_str(str_list, word_list):
    """like is_str_in_words, but reversed. Takes the same args, but removes items from word_list
    that contain no substrings that match any of the items in str_list"""
    keep_list = []
    for w in word_list:
        has_str = False
        for s in str_list:
            if s in w:
                has_str = True
                break
        if has_str:
            keep_list.append(w)
    return keep_list  


def split_or_instr(list_w_bar):
    """takes a list of items that includes a '|' separator and produces a list of lists. Each item
    in the returned list is a list containing the items from its respective side of the '|'."""
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


def add_lists(list_of_lists):
    """performs 'addition' of lists, specifically to address 'or' conditions in the rules.
    [['a', 'b', 'c'], ['d', 'e', 'f']] becomes => ['a', 'b', 'c', 'd', 'e', 'f']"""
    working_list = []
    for sublist in list_of_lists:
        if isinstance(sublist, list):
            for item in sublist:
                working_list.append(item)
        else:
            working_list.append(sublist)
    
    return working_list

def multiply_lists(list_of_lists):
    """performs 'multiplication' of lists, specifically to address 'and' conditions in the rules.
    [['a', 'b'], ['c', 'd']] becomes => ['ac', 'ad', 'bc', 'bd']"""
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
    """creates a list of strings, with each being an acceptable value based on the specified rule.
    It looks up the rule number in the given dict, and interprets the list mapped to it. It will use
    split_or_instr() where it finds a '|' in the rule. And where it finds another rule number,
    it will call itself recursively until it knows which letter to return."""

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

# this list is generated here in order to be referenced by the function below.
# this is not ideal, but helps the program run more quickly
initial_11 = ok_words(rules_dict, 11)

def rule_8_list(dict_of_rules, messages):
    """generates a list of acceptable strings based on the modified rule 8 
    (i.e. it tries 42 | 42 42 | 42 42 42 | ...etc.).  It takes a series of steps after each iteration
    to reduce this list by removing those items that do not match one of the messages.
    This is done to reduce run time."""
    initial_list = ok_words(dict_of_rules, 8)

    msgs_to_check = does_word_contain_str(initial_11, messages)

    max_len = 0
    for msg in messages:
        if len(msg) > max_len:
            max_len = len(msg)

    # function to reduce the size of messages that need to be checked
    trimmed_list = is_str_in_words(initial_list, msgs_to_check)

    # this will hold the strings to be returned by the function
    return_list = []

    # this is a working list of potential words that gets reset after each iteration.
    # empty to start
    wl = ['']

    # function to reduce the size of messages that need to be checked
    msgs_to_check = does_word_contain_str(trimmed_list, msgs_to_check)

    # loops through the most recent vertion of wl[], and 'multiplies' it by the strings 
    # generated by rule 42 ('trimmed+_list')
    empty_wl = 0
    while True:
        if len(wl) == 0:
            empty_wl+= 1
        
        if empty_wl > 5:
            break

        wl_overwrite = []
        mult_list = [wl, trimmed_list]
        new_list = multiply_lists(mult_list)
        
        for poss_word in new_list:
            append_ret = False
            append_wl = False
            if len(poss_word) > max_len:
                #keep_going = False
                break
            
            for okw in msgs_to_check:
                if poss_word in okw:
                    append_ret = True
                    if okw.index(poss_word) <= len(okw) - len(poss_word) - len(trimmed_list[0]):
                        append_wl = True
                    
            if append_ret:
                return_list.append(poss_word)
            if append_wl:
                wl_overwrite.append(poss_word)


        wl = wl_overwrite
        msgs_to_check = does_word_contain_str(wl, msgs_to_check)

    return return_list

# this function gets called here to be referenced by the function below
# not ideal placement, but makes the program run more efficiently
r8 = rule_8_list(rules_dict, msgs)

def rule_11_list(dict_of_rules, messages):
    """works like the rule_8 function above, but has a few additional steps in generating
    the list of strings to address the complexity of the modified rule_11"""
    initial_list = ok_words(dict_of_rules, 11)

    msgs_to_check = does_word_contain_str(r8, messages)

    max_len = 0
    for msg in messages:
        if len(msg) > max_len:
            max_len = len(msg)

    trimmed_list = is_str_in_words(initial_list, msgs_to_check)

    return_list = []
    wl = ['']

    msgs_to_check = does_word_contain_str(trimmed_list, msgs_to_check)

    list_42 = ok_words(dict_of_rules, 42)
    list_31 = ok_words(dict_of_rules, 31)

    empty_wl = 0
    while True:
        if len(wl) == 0:
            empty_wl+= 5
        
        if empty_wl > 3:
            break

        list_42 = is_str_in_words(list_42, msgs_to_check)
        list_31 = is_str_in_words(list_31, msgs_to_check)
        wl = is_str_in_words(wl, msgs_to_check)
        
        wl_overwrite = []
        mult_list = [list_42, wl]
        new_list = multiply_lists(mult_list)

        passed_check_1 = []
        
        for poss_word in new_list:
            if len(poss_word) > max_len:
                #keep_going = False
                break
            for okw in msgs_to_check:
                if poss_word in okw and len(list_42[0]) <= okw.index(poss_word) <= len(okw) - len(poss_word) - (len(list_31[0])):
                    passed_check_1.append(poss_word)
                    break
        
        mult_list = [passed_check_1, list_31]
        new_list = multiply_lists(mult_list)
        msgs_to_check = does_word_contain_str(new_list, msgs_to_check)

        for poss_word in new_list:
            append_ret = False
            append_wl = False
            if len(poss_word) > max_len:
                #keep_going = False
                break
            
            for okw in msgs_to_check:
                if poss_word in okw:
                    append_ret = True
                    if okw.index(poss_word) <= len(okw) - len(poss_word) - len(list_31[0]):
                        append_wl = True
                    
            if append_ret:
                return_list.append(poss_word)
            if append_wl:
                wl_overwrite.append(poss_word)



        wl = wl_overwrite
        msgs_to_check = does_word_contain_str(wl, msgs_to_check)

    return return_list


def solve_p2(messages, dict_of_rules):
    """function to solve 2020 day 19, part 2"""

    r11 = rule_11_list(dict_of_rules, messages)
    
    # reminder, r8 was called earlier in the program

    # generates the full list of strings available by combining those in the modified rule_8 with 
    # those in the modified rule_11.
    mult_list = [r8, r11]
    acceptable_msgs = multiply_lists(mult_list)
    
    # iterates through the list messages in the input, and stores matches in this list
    matches = []
    for msg in messages:
        if msg in acceptable_msgs:
            matches.append(msg)
    
    # the length of this list should be the answer to part 2.
    return len(matches)


ans = solve_p2(msgs, rules_dict)
print(ans)
