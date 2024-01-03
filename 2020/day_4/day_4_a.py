class Passport:
    """models a passport, including its required and optional fields"""

    def __init__(self, byr='', iyr='', eyr='', hgt='', hcl='', ecl='', pid='', cid=''):
        """initializes the passport"""
        self.byr=byr
        self.iyr=iyr
        self.eyr=eyr
        self.hgt=hgt
        self.hcl=hcl
        self.ecl=ecl
        self.pid=pid
        self.cid=cid
    
    def is_valid(self):
        """returns True if the passport has all the required fields populated"""

        if len(self.byr) > 0 and \
            len(self.iyr) > 0 and \
            len(self.eyr) > 0 and \
            len(self.hgt) > 0 and \
            len(self.hcl) > 0 and \
            len(self.ecl) > 0 and \
            len(self.pid) > 0:
            return True
        else:
            return False
    
    def print_fields(self):
        """print the passport's field's and their populated values"""
        print(f"\nbyr: {self.byr}")
        print(f"iyr: {self.iyr}")
        print(f"eyr: {self.eyr}")
        print(f"hgt: {self.hgt}")
        print(f"hcl: {self.hcl}")
        print(f"ecl: {self.ecl}")
        print(f"pid: {self.pid}")
        print(f"cid: {self.cid}")


# holds each passport as one long string
pp_input = []

with open('input.txt') as input_file:
    for line in input_file:
        pp_input.append(line.rstrip()) # might need to add rstrip() back here later

pp_input.append("TEMP_LAST_ROW")

pop_1 = pp_input.pop(0)
pop_2 = pp_input.pop(0)
while True:
    if pop_2 == "TEMP_LAST_ROW":
        pp_input.append(pop_1)
        break

    if pop_2 == "":
        pp_input.append(pop_1)
        pop_1 = pp_input.pop(0)
        pop_2 = pp_input.pop(0)
    else:
        pop_1 = pop_1 + " " + pop_2
        pop_2 = pp_input.pop(0)


# new list to hold each passport as a list of strings. Each string looks like 'field:value'.
pp_input_lists = []

for pp in pp_input:
    split = pp.split(" ")
    pp_input_lists.append(split)


# new list to hold the passports as a list of lists.  Each list will function as a key/value pair
pp_input_list_list = []

# convert each passport in pp_input_lists from a list of strings to a list of dicts
# then store the new passport in pp_input_dicts
for pp in pp_input_lists:
    
    # holds each passport as dictionary
    new_pp_as_list = []

    # reads each passport field in a given passport, and converts the string into a key:value pair
    for pp_field in pp:
        split = pp_field.split(':')
        new_pp_as_list.append(split)

    pp_input_list_list.append(new_pp_as_list)

# new list to hold the passports as a list of Passport class instances
pp_input_class_objs = []

# create an instance of Passport for each passport in the list of dicts, 'pp_input_dicts'
for pp in pp_input_list_list:
    pp_instance = Passport()
    
    for item in pp:
        if item[0] == 'byr':
            pp_instance.byr = item[1]
        if item[0] == 'iyr':
            pp_instance.iyr = item[1]
        if item[0] == 'eyr':
            pp_instance.eyr = item[1]
        if item[0] == 'hgt':
            pp_instance.hgt = item[1]
        if item[0] == 'hcl':
            pp_instance.hcl = item[1]
        if item[0] == 'ecl':
            pp_instance.ecl = item[1]
        if item[0] == 'pid':
            pp_instance.pid = item[1]
        if item[0] == 'cid':
            pp_instance.cid = item[1]
    
    pp_input_class_objs.append(pp_instance)

# new list to hold only valid passports
valid_pps = []

for pp in pp_input_class_objs:
    if pp.is_valid():
        valid_pps.append(pp)

print(f"the number of valid passports is {len(valid_pps)}")
