data_source = "C:\\Users\\Pat\\Documents\\Python\\advent_of_code\\2023\\d1p2_data.txt"
data_list = []
with open(data_source) as f:
    for line in f:
        data_list.append(line.rstrip().lower())

p1_digits = ['0','1','2','3','4','5','6','7','8','9']
p2_digits = ['0','1','2','3','4','5','6','7','8','9','one','two','three','four','five','six', 'seven', 'eight', 'nine']

def get_indices(substring, string, dicty={}):
    """gets indices for a specific substring, so replacing with q's is okay"""

    translations = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    try:
        idx = string.index(substring)
        try:
            translated_substring = translations[substring]
        except:
            translated_substring = substring
        dicty[idx] = translated_substring
        updated_string = string[:idx] + 'q' * len(substring) + string[idx+len(substring):]
        return get_indices(substring, updated_string, dicty)
    except:
        return dicty

def solve(digits):
    dict_list = []
    for s in data_list:
        s_dict = {}
        for digit in digits:
            s_dict = get_indices(digit, s, s_dict)
        dict_list.append(s_dict)

    summy = 0
    for i in dict_list:
        d1 = i[min(i.keys())]
        d2 = i[max(i.keys())]
        # print(f"d1: {d1}; d2: {d2}")
        cal_val = int(d1+d2)
        summy += cal_val

    return summy

print(solve(p1_digits))
print(solve(p2_digits))