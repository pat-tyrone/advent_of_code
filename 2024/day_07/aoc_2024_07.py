import math

def update_result(last_result, bin_operator, next_operand):
    if bin_operator == '0':
        return last_result + next_operand
    elif bin_operator == '1':
        return last_result * next_operand
    else:
        print(f"BAD OPERATOR: {bin_operator}")

def get_trinary(integer):
    if integer == 0:
        return '0'
    num_digits = math.floor(math.log(integer, 3)) + 1
    trinary = ''
    for i in range(num_digits):
        this_three_power = 3**(i)
        next_three_power = 3**(i+1)
        if integer == next_three_power:
            trinary = '10' + trinary
            break
        elif integer < next_three_power:
            next_digit = str(math.floor(integer/this_three_power))
            trinary = next_digit + trinary
        else:
            next_digit = str(int((integer % next_three_power) / this_three_power ))
            trinary = next_digit + trinary
    return trinary

def update_result_p2(last_result, bin_operator, next_operand):
    if bin_operator == '0':
        return last_result + next_operand
    elif bin_operator == '1':
        return last_result * next_operand
    elif bin_operator == '2':
        return int(str(last_result) + str(next_operand))
    else:
        print(f"BAD OPERATOR: {bin_operator}")

expressions = []
with open('input.txt') as f:
    for line in f:
        line_split = line.rstrip().split(': ')
        expressions.append([int(line_split[0]), [int(n) for n in line_split[1].split(' ')]])

# solves P1
p1_ans = 0
for exp in expressions:
    sol = exp[0]
    operands = exp[1]
    num_operators = len(exp[1]) - 1
    for i in range(2 ** num_operators):
        result = operands[0]
        opers_bin = list(bin(i)[2:].zfill(num_operators))
        for j in range(len(opers_bin)):
            result = update_result(result, opers_bin[j], operands[j+1])
            if result > sol:
                break
        if result == sol:
            p1_ans += result
            break
print(f"p1_ans: {p1_ans}")

# solves P2
p2_ans = 0
for exp in expressions:
    sol = exp[0]
    operands = exp[1]
    num_operators = len(exp[1]) - 1
    for i in range(3 ** num_operators):
        result = operands[0]
        opers_bin = list(get_trinary(i).zfill(num_operators))
        for j in range(len(opers_bin)):
            result = update_result_p2(result, opers_bin[j], operands[j+1])
            if result > sol:
                break
        if result == sol:
            p2_ans += result
            break
print(f"p2_ans: {p2_ans}")