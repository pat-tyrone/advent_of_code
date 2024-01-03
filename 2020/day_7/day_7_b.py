import re

class Bag():
    """ a class to model a bag by its color and contents as a list of tuples (color, qty)"""
    def __init__(self, color, contents=[]):
        """initialize the bag"""
        self.color = color
        self.contents = contents
    
    def state_contents(self):
        """returns the allowed bags as a dictionary"""
        for bag in self.contents:
            print(bag)
    
    def open_bag(self):
        """opens the bag and returns just the first level of bags inside as a list of Bag() instances"""
        bags_inside = []
        if len(self.contents) > 0:
            for bag_color in self.contents:
                new_bag = Bag(bag_color[0], bags_and_rules_dict[bag_color[0]])
                for i in range(int(bag_color[1])):
                    bags_inside.append(new_bag)
        return bags_inside


# an empty list to hold the bag rules before any transformations to their format
bag_rules_raw = []

with open('input') as input_file:
    for line in input_file:
        bag_rules_raw.append(line.rstrip())

# splits the list into a list of lists.  each item has a bag color, a sub list of rules (other bags & qty)
bags_and_rules = []

# splits the bag type from its rules and strips unnecessary details from each string
for bag in bag_rules_raw:
    bag = bag.replace('.', '')
    bag = bag.replace(' bags', '')
    bag = bag.replace(' bag', '')
    bag = bag.split(' contain ')
    bags_and_rules.append(bag)

# splits the rule set into a sub-list of individual rules
for bag in bags_and_rules:
    rules = bag.pop()
    rules_split = rules.split(', ')
    bag.append(rules_split)

# converts the rules into a list of tuples (color, qty)
# final version of bags_and_rules is a list of 2-item lists. 
# 2nd item is a list of tuples representing the bags inside the bag
# each tuple is (color, qty) combo
for bag in bags_and_rules:
    rules = bag.pop()
    rules_reformatted = []

    for rule in rules:
        if rule != 'no other':
            num_bag = rule.replace(' ', '|', 1)
            num_bag = num_bag.split('|')
            rules_tup = (num_bag[1], num_bag[0])
            rules_reformatted.append(rules_tup)

    bag.append(rules_reformatted)

# a list of dictionaries as an alternate reference to bags_and_rules
# possible unnecessary
bags_and_rules_dict = {}
for bag in bags_and_rules:
    bags_and_rules_dict[bag[0]] = bag[1]

# a list of Bag() instances
bags = []
for bag in bags_and_rules:
    new_bag = Bag(bag[0], bag[1])
    bags.append(new_bag)


total_bags = []

gold_bag = Bag('shiny gold', bags_and_rules_dict['shiny gold'])

bags_to_open = gold_bag.open_bag()

while bags_to_open:
    current_bag = bags_to_open.pop(0)
    total_bags.append(current_bag)
    more_bags = current_bag.open_bag()
    for each_bag in more_bags:
        bags_to_open.append(each_bag)
    
print(len(total_bags))