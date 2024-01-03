import statistics

class Ticket:
    """models a boarding pass"""

    def __init__(self, ticket_num):
        """initialize th boarding pass with ticket number as the required argument"""
        self.ticket_num = ticket_num
        self.row_num = 0
        self.col_num = 0
        self.seat_id = 0

        # stores the ticket number as a list of individual characters
        self.tn_as_list = []
        for char in self.ticket_num:
            self.tn_as_list.append(char.upper())
    
    def determine_row(self):
        """returns the row, based on the ticket_num"""

        relevant_chars = []
        for char_num in range(7):
            relevant_chars.append(self.tn_as_list[char_num])
        
        row = 0
        digit = len(relevant_chars) - 1
        for char in relevant_chars:
            if char == 'F':
                adder = 0
            elif char == 'B':
                adder = 1
            else:
                break
            row += (2**digit) * adder
            digit -= 1
        
        self.row_num = row
        return row

    def determine_col(self):
        """returns the column, based on the ticket_num"""

        relevant_chars = []
        for char_num in range(3):
            relevant_chars.append(self.tn_as_list[char_num + 7])
        
        col = 0
        digit = len(relevant_chars) - 1
        for char in relevant_chars:
            if char == 'L':
                adder = 0
            elif char == 'R':
                adder = 1
            else:
                break
            col += (2**digit) * adder
            digit -= 1
        
        self.col_num = col
        return col
    
    def determine_seat_id(self):

        x = self.determine_row()
        y = self.determine_col()

        self.seat_id = (x * 8) + y
        return self.seat_id
    
    # this may not work until other functions are moved into __init__
    def pop_vars(self):
        """populate the variables row_num, col_num, and seat_id for self"""
        #self.determine_row()
        #self.determine_col()
        self.determine_seat_id()


tickets_input = []

try:
    with open('input') as f:
        for line in f:
            tickets_input.append(line.rstrip())
except FileNotFoundError:
    print('something went wrong when opening the file')

# new list to hold the tickets as instances of the class Ticket()
ticket_instances = []

# iterate through the list of ticket numbers and create Ticket instances, and add each to ticket_instances[]
for ticket in tickets_input:
    t_inst = Ticket(ticket)
    t_inst.pop_vars()

    ticket_instances.append(t_inst)

# new list to hold just the seat IDs
seat_ids = []

for tic in ticket_instances:
    seat_ids.append(tic.seat_id)

print(f"the highest seat_id is {max(seat_ids)}")

seat_ids.sort()

for value in range(len(seat_ids)-1):
    if seat_ids[value] + 1 != seat_ids[value+1] and \
        seat_ids[value+1] != seat_ids[value+1] - 1:
        print(f"your seat # is {(seat_ids[value] + seat_ids[value+1]) / 2}")
