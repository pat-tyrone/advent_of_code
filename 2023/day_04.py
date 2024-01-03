aoc_data = []
with open('d4_data.txt') as f:
    for line in f:
        aoc_data.append(line.rstrip())


def get_score(winning_numbers, my_numbers):
    win_count = 0
    for x in winning_numbers:
        for y in my_numbers:
            if int(x) == int(y):
                win_count += 1
    
    if win_count != 0:
        return 2**(win_count - 1)
    else:
        return 0

def copy_cards(card_dict):
    win_count = 0
    for x in card_dict["win_nums"]:
        for y in card_dict["my_nums"]:
            if int(x) == int(y):
                win_count += 1
    
    return {"wins": win_count, "instances": card_dict["instance_count"]}


cards =  []
for line in aoc_data:
    card_dict = {}
    split_on_colon = line.split(': ')
    card_dict["card_num"] = split_on_colon[0].replace('Card', '').replace(' ', '')
    number_sets = split_on_colon[1].strip().replace('  ',  ' 0').split('|')
    card_dict["win_nums"] = number_sets[0].strip().split(' ')
    card_dict["my_nums"] = number_sets[1].strip().split(' ')

    card_dict["instance_count"] = 1

    cards.append(card_dict)

p1_answer = 0
for card in cards:
    p1_answer += get_score(card["win_nums"], card["my_nums"])

print(p1_answer)

p2_answer = 0
for i in range(len(cards)):
    
    p2_answer += cards[i]["instance_count"]
    copy_instructions = copy_cards(cards[i])
    cards_to_copy = copy_instructions["wins"]
    range_max = min(i+1+cards_to_copy, len(cards))
    for j in range(i+1, range_max):
        cards[j]["instance_count"] += cards[i]["instance_count"]

print(p2_answer)