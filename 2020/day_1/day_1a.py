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
counter_3=2

while counter_1 < len(expenses)-2:
    x = expenses[counter_1]
    y = expenses[counter_2]
    z = expenses[counter_3]
    test = x + y + z

    if test == 2020:
        correct_entries.append(x)
        correct_entries.append(y)
        correct_entries.append(z)
        answer = x*y*z
    
    attempts.append(test)
    counter_3 += 1

    if counter_3 ==  len(expenses):
        counter_2 += 1
        counter_3 = counter_2 +1
    
    if counter_2 == len(expenses)-1:
        counter_1 += 1
        counter_2 = counter_1 + 1
        counter_3 = counter_1 + 2
    
print(f"\nthere were {len(expenses)} entries in the file.")
print(f"\nthe total number of attempts was {len(attempts)}")
print(correct_entries)
print(f"\nthe entries that summed to 2020 were {correct_entries[0]}, {correct_entries[1]} and {correct_entries[2]}.")
print(f"\nthe product of these two numbers is {answer}\n")

if len(correct_entries) > 3:
    print("something went wrong.  maybe more than 1 correct answer")