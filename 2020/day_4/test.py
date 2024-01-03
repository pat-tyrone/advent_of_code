import re

test_list = ['pat', '44in', 'abcin', '43cm', '456incm', '567', '4567ppws', 'this is a test 44in', '45676cm char at end']


for string in test_list:
    if (re.search('^\d*(in|cm)$', string)):
        new_str = re.sub('(in|cm)', '', string)
        print(new_str)

"""
for string in test_list:
    split = re.split("[0-9]+(in|cm)", string)
    print(split)jj
"""