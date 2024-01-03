import re

def extract_paren_exp(expression):
    """finds outer parens and returns expression within (incl inner parens) as a string
    must start with a '(' """
    op_calc = 0
    char_idx = 0
    for char in expression:
        if char == '(':
            op_calc += 1
        elif char == ')':
            op_calc -= 1

        if op_calc == 0:
            break
        else:
            char_idx += 1
    cp_pos = char_idx

    return (expression[1:cp_pos])

def solve_expression(starting_expression, running_solution=''):
    """solve an expression passed as a string"""
    
    expression = running_solution + starting_expression    

    # define first_num, either as the result of a paren_exp, or as the next integer in the expression
    next_char = expression[:1]
    if next_char == '(':
        paren_exp = extract_paren_exp(expression)
        first_num = str(solve_expression(paren_exp))
        expression = expression[len(paren_exp) + 2:].lstrip()
    else:
        first_num = re.match('\d+', expression).group(0)
        expression = expression.replace(first_num, '', 1).lstrip()

    # define the operator
    operator = expression[:1]
    expression = expression.replace(operator, '', 1).lstrip()

    # define second_num just like first_num
    next_char = expression[:1]
    if next_char == '(':
        paren_exp = extract_paren_exp(expression)
        second_num = str(solve_expression(paren_exp))
        expression = expression[len(paren_exp) + 2:].lstrip()
    else:
        second_num = re.match('\d+', expression).group(0)
        expression = expression.replace(second_num, '', 1).lstrip()

    # with first_num, operator, and second_num defined, perform computation
    if operator == '+':
        run_sol = int(first_num) + int(second_num)
    elif operator == '*':
        run_sol = int(first_num) * int(second_num)
    else:
        print("ERROR")

    # if there is more to solve, pass the remaining expression and the solution to above in recursive call
    if len(expression) > 0:
        solution = solve_expression(expression, str(run_sol))
    else: 
        solution = run_sol
    
    return solution

hw_in = []

with open('input.txt') as hw_file:
    for line in hw_file:
        hw_in.append(line.strip())

p1_ans = 0

for hw_prob in hw_in:
    hw_ans = solve_expression(hw_prob)
    p1_ans += hw_ans

print(p1_ans)