expenses = []

with open('input.txt') as input_file:
    for line in input_file:
        expenses.append(int(line))

#print(len(expenses))

answer=0
attempts = []
correct_entries=[]
counter_1=0
counter_2=1

while counter_1 < len(expenses)-1:
    x = expenses[counter_1]
    y = expenses[counter_2]
    test = x + y
    #print(test)

    if test == 2020:
        correct_entries.append(x)
        correct_entries.append(y)
        answer = x*y
    
    attempts.append(test)
    counter_2 += 1

    if counter_2 >=  len(expenses):
        counter_1 += 1
        counter_2 = counter_1 + 1
    
print(f"\nthere were {len(expenses)} entries in the file.")
print(f"\nthe total number of attempts was {len(attempts)}")
print(f"\nthe entries that summed to 2020 were {correct_entries[0]} and {correct_entries[1]}.")
print(f"\nthe product of these two numbers is {answer}")

if len(correct_entries) > 2:
    print("something went wrong.  maybe more than 1 correct answer")

