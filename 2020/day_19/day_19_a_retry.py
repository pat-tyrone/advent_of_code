
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


def ok_words(dict_of_rules, rule_num):
    """creates a list of strings, with each being an acceptable value based on the specified rule
    no rule argument will (eventually) return a full list of acceptable words"""

    return_list = []

    start_list = dict_of_rules[str(rule_num)]

    # print(start_list)

    for item in start_list:

        if item == '|':
            return_list.append(item)
        
        else:

            instruction = dict_of_rules[item]

            if instruction[0] in ['a', 'b']:
                return_list.append(instruction)
            else:
                list_step = []
                for item in instruction:
                    if item != '|':
                        append_this = ok_words(dict_of_rules, item)
                        list_step.append(append_this)
                return_list.append(list_step)

    return return_list


print(rules_dict)
words_test = ok_words(rules_dict, 0)

print(words_test)

print("\nOG:")
print(words_test)

words_test = split_or_instr(words_test)

print("\nsplit on OR:")
print(words_test)

# words_test = remove_sublists(words_test)

# for line in words_test:
#     print(line)