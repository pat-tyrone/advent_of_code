from statistics import mode

aoc_data = []
with open('data_07.txt') as f:
    for line in f:
        aoc_data.append(line.rstrip())

def count_cards(cards):
    cc = {}

    for card in cards:
        if card not in cc.keys():
            cc[card] = 1
        else:
            cc[card] += 1
    

    return cc

def hand_rank(cc_dict):
    """
    hand types and rank values:
    
    Five of a kind - 7
    Four of a kind - 6
    Full house - 5
    Three of a kind - 4
    Two pair - 3
    One pair - 2
    High card - 1
    
    """
    dv = list(cc_dict.values())
    if 5 in dv:
        return 7
    elif 4 in dv:
        return 6
    elif 3 in dv:
        if 2 in dv:
            return 5
        else:
            return 4
    elif dv.count(2) == 2:
        return 3
    elif 2 in dv:
        return 2
    else:
        return 1


def assign_jokers(hand):
    j_cards = []
    others = []
    for card in hand:
        if card == 0:
            j_cards.append(card)
        else:
            others.append(card)
    if others:
        hm = mode(others)
    else:
        hm = 0
    
    for j in j_cards:
        others.append(hm)
    
    return others


hands = []

card_map = {
    'A': 13, 
    'K': 12, 
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

for line in aoc_data:
    hand = {}
    line_split = line.split()
    hand['cards'] = [card_map[card] for card in line_split[0]]
    hand['bid'] = int(line_split[1])
    hands.append(hand)

hands_by_rank = {
    7: [],
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: []
}

for i, v in enumerate(hands):
    hr = hand_rank(count_cards(v['cards']))
    hands_by_rank[hr].append((i,v))

for k in hands_by_rank.keys():
    hands_by_rank[k] = sorted(hands_by_rank[k], key=lambda x: (x[1]['cards'][0], x[1]['cards'][1], x[1]['cards'][2], x[1]['cards'][3], x[1]['cards'][4]), reverse=True)


winnings = 0
next_rank = len(aoc_data)

for k, v in hands_by_rank.items():
    for hand in v:
        bid = hand[1]['bid']
        win_amt = next_rank * bid
        winnings += win_amt
        next_rank += -1

# p1 answer
print(winnings)


hands_p2 = []

card_map = {
    'A': 13, 
    'K': 12, 
    'Q': 11,
    'J': 0,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

for line in aoc_data:
    try:
        hand = {}
        line_split = line.split()
        cards_as_list = [card_map[card] for card in line_split[0]]
        hand['cards_for_ties'] = cards_as_list
        hand['bid'] = int(line_split[1])
        hand['cards_for_rank'] = assign_jokers(cards_as_list)
        hands_p2.append(hand)
    except:
        print(line)
        break

hands_by_rank_p2 = {
    7: [],
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: []
}

for i, v in enumerate(hands_p2):
    hr = hand_rank(count_cards(v['cards_for_rank']))
    hands_by_rank_p2[hr].append((i,v))

for k in hands_by_rank_p2.keys():
    hands_by_rank_p2[k] = sorted(hands_by_rank_p2[k], key=lambda x: (x[1]['cards_for_ties'][0], x[1]['cards_for_ties'][1], x[1]['cards_for_ties'][2], x[1]['cards_for_ties'][3], x[1]['cards_for_ties'][4]), reverse=True)


winnings_p2 = 0
next_rank = len(aoc_data)

for k, v in hands_by_rank_p2.items():
    for hand in v:
        bid = hand[1]['bid']
        win_amt = next_rank * bid
        winnings_p2 += win_amt
        next_rank += -1

# p2 answer
print(winnings_p2)