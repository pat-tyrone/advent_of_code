
lof = []


with open('input.txt') as lof_input:
    for line in lof_input:
        lof_i = line.strip()
        lof_i = lof_i.split(' (contains ')
        lof_i[0] = lof_i[0].split()
        lof_i[1] = lof_i[1].replace(')', '')
        lof_i[1] = lof_i[1].replace(',', '')
        lof_i[1] = lof_i[1].split()
        lof.append(lof_i)

ingredients = []
allergens = []

for line in lof:
    for ingredient in line[0]:
        ingredients.append(ingredient)
    for allergen in line[1]:
        allergens.append(allergen)

# for line in lof:
#     print(line)

poss_allers = {}
known_allers = {}
counter = 0
while True:
    counter += 1
    # print(f"\n{counter}")
    # print(f"\n{known_allers}\n")

    check = len(known_allers.keys())

    for food in lof:
        # print(f"\nchecking: {food}")
        for allergen in food[1]:
            # print(f"\tallergen: {allergen}")
            if allergen in known_allers.keys():
                # print(f"\t\tknown allergen is in: {known_allers[allergen]}")
                break
            elif allergen in poss_allers.keys():
                # print(f"\t\tpossible ingreds, pre check: {poss_allers[allergen]}")
                new_ingreds = []
                for ingred in food[0]:
                    # print(f"\t\tnew ingred check: {ingred}")
                    if ingred in poss_allers[allergen]:
                        # print("\t\t\talready mapped; still a possibility")
                        new_ingreds.append(ingred)
                    # else:
                        # print("\t\t\tthis ingred is out.")
                if len(new_ingreds) == 1:
                    # print(f"\t\t\t\tallergen/ingred MATCHED********")
                    # print(f"\t\t\t\t\t\t\tmapping {ingred} to {allergen}")
                    known_allers[allergen] = new_ingreds[0]
                else:
                    # print(f"\t\t\t\tnew poss_allers for {allergen}: {new_ingreds}")
                    poss_allers[allergen] = new_ingreds
            else:
                # print("\t\tmapping allergen for the first time:")
                if len(food) == 1:
                    # print(f"\t\t\tnow a known_aller")
                    known_allers[allergen] = food[0]
                else:
                    # print("\t\t\tnew poss_aller mapping")
                    poss_allers[allergen] = food[0]

    # for line in lof:
    #     print(line)

    print("\nbeginning removal sequence\n")
    for i in range(len(lof)):
        print(f"i = {i}")
        print(f"lof[i] = {lof[i]}")
        print(f"known_allers.keys() = {known_allers.keys()}")
        for aller in lof[i][1]:
            print(f"\n\tchecking aller: {aller}")
            if aller in known_allers.keys():
                if counter == 2:
                    print(f"\n\tknown_allers: {known_allers}\n")
                    print(f"\ni = {i}; checking for removal: {lof[i]}")
                    print(f"removed {known_allers[aller]}, {aller} from:\n\t{lof[i]}")
                lof[i][0].remove(known_allers[aller])
                lof[i][1].remove(aller)
        for ingred in lof[i][0]:
            if ingred in known_allers.values():
                if ingred == 'smfz':
                    print(f"\n\n\n\t\t\REMOVING SMFZ from i={i}\n\n\n")
                    print(lof[i])
                lof[i][0].remove(ingred)

    # print("\nlof, post removals:\n")
    # for line in lof:
    #     print(line)
    
    # print(f"\nknown_allers:\n\t{known_allers}\n")

    if len(known_allers.keys()) == check:
        break

# for line in lof:
#     print(line)

# print("\n")

no_allers = []
poss_no_allers = []
prob_allers = []
for food in lof:
    if len(food[1]) == 0:
        for ingred in food[0]:
            poss_no_allers.append(ingred)
    else:
        for ingred in food[0]:
            prob_allers.append(ingred)

# print(poss_no_allers)
# print(prob_allers)

for ingred in poss_no_allers:
    if ingred not in prob_allers:
        no_allers.append(ingred)

# print(no_allers)
print(len(no_allers))
