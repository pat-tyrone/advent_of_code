# departure location: 45-609 or 616-954
# departure station: 32-194 or 211-972
# departure platform: 35-732 or 744-970
# departure track: 40-626 or 651-952
# departure date: 44-170 or 184-962
# departure time: 49-528 or 538-954
# arrival location: 36-448 or 464-956
# arrival station: 48-356 or 373-972
# arrival platform: 25-118 or 132-954
# arrival track: 43-703 or 719-965
# class: 29-822 or 828-961
# duration: 25-131 or 151-967
# price: 44-784 or 794-958
# route: 25-498 or 511-951
# row: 44-905 or 916-973
# seat: 26-756 or 777-960
# train: 36-803 or 819-954
# type: 33-318 or 335-967
# wagon: 46-558 or 570-969
# zone: 47-249 or 265-972

rules = []

with open('rules.txt') as the_rules:
    for line in the_rules:
        rules.append(line.strip())

fields = []
first_ranges = []
second_ranges = []

for rule in rules:
    split_field = rule.split(': ')
    fields.append(split_field[0])

    split_or = split_field[1].split(' or ')
    first_ranges.append(split_or[0])
    second_ranges.append(split_or[1])

both_ranges = [first_ranges, second_ranges]
range_list = []

for rng in both_ranges:
    for i in rng:
        split = i.split('-')
        range_min = int(split[0])
        range_max = int(split[1])
        min_max = [range_min, range_max]
        range_list.append(min_max)


nb_tix = []

with open('nearby_tix.txt') as tix:
    for tick in tix:
        nb_tix.append(tick.strip())

# for tick in nb_tix[0:5]:
#     print(type(tick))
#     print(tick)

for tick in range(len(nb_tix)):
    pop = nb_tix.pop(0)
    fields = pop.split(',')
    field_ints = []

    for field in fields:
        field_ints.append(int(field))
    
    nb_tix.append(field_ints)


tse_list = []
tser = 0

for tick in nb_tix:
    #print(f"\ntrying ticket: {tick}")
    for num in tick:
        #print(f"\ttrying num: {num}")
        tse = False
        for rng in range_list:
            tse = True
            if num >= rng[0] and num <= rng[1]:
                #print(f"\t\tnum ok, b/w: {rng}")
                tse = False
                break
            
            
        if tse:
            #print(f"\t\tnum failed.")
            tser += num
            tse_list.append(num)
            

print(tser)
