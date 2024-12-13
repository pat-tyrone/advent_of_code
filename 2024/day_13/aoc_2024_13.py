import re
import sympy as sp

def get_digits(string):
    """takes the full line as a string, returns a 2 item list of the x and y values"""
    return ([int(x) for x in re.findall('\\d+', string)])

# create a dict for each machine, store them in machines[]
machines = []
with open('input.txt') as f:
    temp_machines = f.read().split('\n\n')
    for tm in temp_machines:
        tm_split = tm.split('\n')
        machine = {'a': get_digits(tm_split[0]), 'b': get_digits(tm_split[1])}
        machine['prize_1'] = [x for x in get_digits(tm_split[2])]
        machine['prize_2'] = [10000000000000 + x for x in get_digits(tm_split[2])]
        machines.append(machine)

# define the cost for each button push; store in this 1x2 matrix
cost = sp.Matrix([[3,1]]) 

# iterate over all machines (structured as matrices--augmented with prize coordinate vector), row reduce, perform matrix mult. to get cost in tokens
p1_ans = 0
p2_ans = 0
for machine in machines:
    button_vectors = sp.Matrix([machine['a'], machine['b']]).transpose() # need to transpose b/c solution vector has button presses, so columns need to correspond to buttons
    P_1 = button_vectors.col_insert(2, sp.Matrix(machine['prize_1']))
    P_2 = button_vectors.col_insert(2, sp.Matrix(machine['prize_2']))
    
    # solution vectors for parts 1 and 2 (i.e. number of button presses)
    button_presses_1 = P_1.rref()[0].col(2)
    button_presses_2 = P_2.rref()[0].col(2)

    if all(element.is_integer for element in button_presses_1):
        machine_cost = cost * button_presses_1
        p1_ans += machine_cost[0,0]
    if all(element.is_integer for element in button_presses_2):
        machine_cost = cost * button_presses_2
        p2_ans += machine_cost[0,0]

print(f"p1_ans: {p1_ans}")
print(f"p2_ans: {p2_ans}")