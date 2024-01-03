import re

def apply_parens(expression):
    """put parens around addition in the expression so it is prioritized over multiplication"""
    exp = expression
    add_count = exp.count('+')
    add_exp = re.search('\d+\s\+\s\d+', expression)
    return add_exp

    

def solve_expression(starting_expression, running_solution=''):
    """solve an expression passed as a string"""

    close_parens_test = starting_expression[:1]

    if close_parens_test == ')':
        solution = int(running_solution)
        expression = starting_expression[1:].lstrip()

        return running_solution

    else:
        expression = running_solution + starting_expression
        next_char = expression[:1]

        if next_char == '(':
            expression = expression[1:]
            op_calc = 1
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

            first_num =  solve_expression(expression)
            expression = expression[cp_pos+1:].lstrip()

        else:
            first_num = re.match('\d+', expression).group(0)
            expression = expression.replace(first_num, '', 1).lstrip()
            
        operator = expression[:1]

        expression = expression.replace(operator, '', 1).lstrip()

        next_char = expression[:1]
        if next_char == '(':
            expression = expression[1:]

            op_calc = 1
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

            second_num = solve_expression(expression)
            expression = expression[cp_pos+1:].lstrip()
    
        else:       
            second_num = re.match('\d+', expression).group(0)
            expression = expression.replace(second_num, '', 1).lstrip()

        if operator == '+':
            run_sol = int(first_num) + int(second_num)
        elif operator == '*':
            run_sol = int(first_num) * int(second_num)
        else:
            print("ERROR")
    

        if len(expression) > 0:
            solution = solve_expression(expression, str(run_sol))
        else: 
            solution = run_sol
        
        return solution

hw_in = []

with open('input.txt') as hw_file:
    for line in hw_file:
        hw_in.append(line.strip())


test_prob = '5 * 9 + 7 (8 * 3 + 9 + 3 * 4 * 3)'

print(apply_parens(test_prob))







# p1_ans = 0

# for hw_prob in hw_in:
#     hw_ans = solve_expression(hw_prob)
#     p1_ans += hw_ans

# print(p1_ans)