def assign_seat_nums(chart):
    """creates a dictionary that is a map of seat addresses and their occupied status
    like this: {seat_address, 0} for unoccupied or floor, {seat_address, 1} for occupied"""
    
    seat_count = 1
    sa_map = []
    seat_dict = {}

    for row in chart:
        row_map = []
        
        for seat in row:
            seat_state = 0
            if seat == 'L' or seat == '.':
                seat_state = 0
            elif seat == '#':
                seat_state = 1
            else:
                print("SEAT STATE ERROR")
                break

            sa = seat_count
            seat_dict[sa] = seat_state
            row_map.append(sa)
            seat_count += 1
        sa_map.append(row_map)

    return seat_dict

def assign_seat_nums_map(chart):
    """like the function above, but retains 'L', '#', and '.' for unoccupied, occupied, and floor, respectively"""
    seat_count = 1
    seat_dict = {}

    for row in chart:
        
        for seat in row:
            sa = seat_count
            seat_dict[sa] = seat
            seat_count += 1

    return seat_dict


def assign_seat_address(chart, row_num, seat_num):
    """takes a chart in list format, and row/seat numbers and assigns an address 1-n
    for a chart with n seats"""
    total_rows = len(chart)
    spr = len(chart[0])
    address = ((row_num-1) * spr) + seat_num

    return address

def row_and_seat(chart, seat_address):
    """converts a seat address to a (row_num, seat_num) tuple"""
    total_rows = len(chart)
    spr = len(chart[0])
    row_num = 0
    seat_num = 0

    if seat_address <= spr:
        row_num = 1
    elif seat_address % spr == 0:
        row_num = seat_address / spr
    else:
        row_num = (seat_address - (seat_address % spr)) / spr + 1
    
    if seat_address % spr == 0:
        seat_num = spr
    else:
        seat_num = seat_address % spr
    
    return (row_num, seat_num)


def next_seat_up(chart, seat_address):
    """returns the seat_address of the next seat up"""
    sd = assign_seat_nums(chart)
    ras = row_and_seat(chart, seat_address)
    if ras[0] == 1:
        nsu = assign_seat_address(chart, ras[0], ras[1])
    else:
        nsu = assign_seat_address(chart, ras[0]-1, ras[1])
    return nsu

def next_seat_down(chart, seat_address):
    """returns the seat_address of the next seat down"""
    sd = assign_seat_nums(chart)
    ras = row_and_seat(chart, seat_address)
    if ras[0] == len(chart):
        nsd = assign_seat_address(chart, ras[0], ras[1])
    else:
        #print("NSR ELSE")
        nsd = assign_seat_address(chart, ras[0]+1, ras[1])
    return nsd

def next_seat_left(chart, seat_address):
    """returns the seat_address of the next seat to the left"""
    sd = assign_seat_nums(chart)
    ras = row_and_seat(chart, seat_address)
    if ras[1] == 1:
        nsl = assign_seat_address(chart, ras[0], ras[1])
    else:
        nsl = assign_seat_address(chart, ras[0], ras[1]-1)
    return nsl

def next_seat_right(chart, seat_address):
    """returns the seat_address of the next seat to the right"""
    sd = assign_seat_nums(chart)
    ras = row_and_seat(chart, seat_address)
    if ras[1] == len(chart[0]):
        #print("NSR IF")

        nsr = assign_seat_address(chart, ras[0], ras[1])
    else:
        #print("NSR ELSE")

        nsr = assign_seat_address(chart, ras[0], ras[1]+1)
    return nsr

def nsu_cont (chart, seat_address):
    """keeps checking up until it sees a seat, and return that seat address"""
    sd = assign_seat_nums_map(chart)
    keep_going = True
    seat = seat_address
    while keep_going:
        try:
            ns_ref = seat
            ns_ref_ras = row_and_seat(chart, seat)
            ns = next_seat_up(chart, seat)
            ras = row_and_seat(chart, ns)

            if ras != (ns_ref_ras[0]-1, ns_ref_ras[1]):
                seat = ns_ref
                keep_going = False
            else:
                seat = ns
                
            if sd[seat] != '.':
                keep_going = False

        except:
            break
    return seat

def nsd_cont (chart, seat_address):
    """keeps checking down until it sees a seat, and return that seat address"""
    sd = assign_seat_nums_map(chart)
    keep_going = True
    seat = seat_address
    while keep_going:
        try:
            ns_ref = seat
            ns_ref_ras = row_and_seat(chart, seat)
            ns = next_seat_down(chart, seat)
            ras = row_and_seat(chart, ns)

            if ras != (ns_ref_ras[0]+1, ns_ref_ras[1]):
                seat = ns_ref
                keep_going = False
            else:
                seat = ns
                
            if sd[seat] != '.':
                keep_going = False

        except:
            break
    return seat

def nsl_cont (chart, seat_address):
    """keeps checking left until it sees a seat, and return that seat address"""
    sd = assign_seat_nums_map(chart)
    keep_going = True
    seat = seat_address
    while keep_going:
        try:
            ns_ref = seat
            ns_ref_ras = row_and_seat(chart, seat)
            ns = next_seat_left(chart, seat)
            ras = row_and_seat(chart, ns)

            if ras != (ns_ref_ras[0], ns_ref_ras[1]-1):
                seat = ns_ref
                keep_going = False
            else:
                seat = ns
                
            if sd[seat] != '.':
                keep_going = False

        except:
            break
    return seat

def nsr_cont (chart, seat_address):
    """keeps checking right until it sees a seat, and return that seat address"""
    sd = assign_seat_nums_map(chart)
    keep_going = True
    seat = seat_address
    while keep_going:
        try:
            ns_ref = seat
            ns_ref_ras = row_and_seat(chart, seat)
            ns = next_seat_right(chart, seat)
            ras = row_and_seat(chart, ns)

            if ras != (ns_ref_ras[0], ns_ref_ras[1]+1):
                seat = ns_ref
                keep_going = False
            else:
                seat = ns
                
            if sd[seat] != '.':
                keep_going = False

        except:
            break
    return seat

def nsur_cont (chart, seat_address):
    """keeps checking up and to the right until it sees a seat, and return that seat address"""
    sd = assign_seat_nums_map(chart)
    keep_going = True
    seat = seat_address
    while keep_going:
        try:
            #print('trying')
            ns_ref = seat
            ns_ref_ras = row_and_seat(chart, seat)
            ns = next_seat_up(chart, seat)
            #print(f"NSU: {row_and_seat(chart, ns)}")
            ns = next_seat_right(chart, ns)
            #print(f"NS: {row_and_seat(chart, ns)}")

            #print(f"NSR: {row_and_seat(chart, ns)}")
            ras = row_and_seat(chart, ns)
            #print(f"NSUR: {row_and_seat(chart, ns)}")

            if ras != (ns_ref_ras[0]-1, ns_ref_ras[1]+1):
                #print("validity check failed")
                seat = ns_ref
                keep_going = False
            else:
                #print("valid")
                seat = ns
                
            if sd[seat] != '.':
                #print("found a seat")
                keep_going = False

        except:
            #print("EXCEPT")
            break
    return seat

def nsdr_cont (chart, seat_address):
    """keeps checking down and to the right until it sees a seat, and return that seat address"""
    sd = assign_seat_nums_map(chart)
    keep_going = True
    seat = seat_address
    while keep_going:
        try:
            ns_ref = seat
            ns_ref_ras = row_and_seat(chart, seat)
            ns = next_seat_down(chart, seat)
            ns = next_seat_right(chart, ns)
            ras = row_and_seat(chart, ns)

            if ras != (ns_ref_ras[0]+1, ns_ref_ras[1]+1):
                # print("IF:")
                seat = ns_ref
                keep_going = False
            else:
                # print("ELSE")
                seat = ns
                
            if sd[seat] != '.':
                # print("SECOND IF")
                keep_going = False

        except:
            # print("EXCEPTED")
            break
    # print(row_and_seat(chart, seat))
    return seat

def nsdl_cont (chart, seat_address):
    """keeps checking down and to the left until it sees a seat, and return that seat address"""
    sd = assign_seat_nums_map(chart)
    keep_going = True
    seat = seat_address
    while keep_going:
        try:
            ns_ref = seat
            ns_ref_ras = row_and_seat(chart, seat)
            ns = next_seat_down(chart, seat)
            ns = next_seat_left(chart, ns)
            ras = row_and_seat(chart, ns)

            if ras != (ns_ref_ras[0]+1, ns_ref_ras[1]-1):
                seat = ns_ref
                keep_going = False
            else:
                seat = ns
                
            if sd[seat] != '.':
                keep_going = False

        except:
            break
    return seat

def nsul_cont (chart, seat_address):
    """keeps checking up and to the left until it sees a seat, and return that seat address"""
    sd = assign_seat_nums_map(chart)
    keep_going = True
    seat = seat_address
    while keep_going:
        try:
            ns_ref = seat
            ns_ref_ras = row_and_seat(chart, seat)
            ns = next_seat_up(chart, seat)
            ns = next_seat_left(chart, ns)
            ras = row_and_seat(chart, ns)

            if ras != (ns_ref_ras[0]-1, ns_ref_ras[1]-1):
                seat = ns_ref
                keep_going = False
            else:
                seat = ns
                
            if sd[seat] != '.':
                keep_going = False

        except:
            break
    return seat



def shuffle_seats(chart):
    """iterates through entire seat map, looking in each direction to see if the seats around 
    are occupied.  It then applies the rules given in the problem and returns a new seat map
    reflecting what happens to each seat after a single round of changes"""
    sd = assign_seat_nums(chart)
    new_sc = []
    total_rows = len(chart)
    spr = len(chart[0])
    row_num = 1
    seat_num = 1
    seat_count = 1
    changes = 0

    for row in chart:
        new_sc_row = []
        seat_num = 1

        for seat in row:

            # print(f"\nseat_count: {seat_count}")

            if seat == '.':
                new_sc_row.append(seat)
            
            else:


                # first row
                if row_num == 1:

                    # left-most seat
                    if seat_num == 1:

                        # print("1L")

                        nbrs = [nsr_cont(chart, seat_count), nsd_cont(chart, seat_count), nsdr_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:
                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check
                    # right-most seat
                    elif seat_num == spr:

                        # print("1R")

                        nbrs = [nsl_cont(chart, seat_count), nsd_cont(chart, seat_count), nsdl_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:
                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check
                    # all middle seats
                    else:

                        # print("1C")

                        nbrs = [nsl_cont(chart, seat_count), nsr_cont(chart, seat_count), nsdl_cont(chart, seat_count), nsd_cont(chart, seat_count), nsdr_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:
                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check

                # last row
                elif row_num == total_rows:

                    # left-most seat
                    if seat_num == 1:

                        # print("-1L")

                        nbrs = [nsu_cont(chart, seat_count), nsr_cont(chart, seat_count), nsur_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:
                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check
                    
                    # right-most seat
                    elif seat_num == spr:

                        # print("-1R")

                        nbrs = [nsl_cont(chart, seat_count), nsu_cont(chart, seat_count), nsul_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:
                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check

                    # all middle seats
                    else:

                        # print("-1C")

                        nbrs = [nsl_cont(chart, seat_count), nsr_cont(chart, seat_count), nsul_cont(chart, seat_count), nsu_cont(chart, seat_count), nsur_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:

                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check

                # all other rows
                else:

                    # left-most seat
                    if seat_num == 1:

                        # print("0L")

                        nbrs = [nsu_cont(chart, seat_count), nsur_cont(chart, seat_count), nsr_cont(chart, seat_count), nsdr_cont(chart, seat_count), nsd_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:
                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check
                    
                    # right-most seat
                    elif seat_num == spr:

                        # print("0R")

                        nbrs = [nsu_cont(chart, seat_count), nsul_cont(chart, seat_count), nsl_cont(chart, seat_count), nsdl_cont(chart, seat_count), nsd_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:
                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check

                    # all middle seats
                    else:

                        # print("0C")

                        nbrs = [nsul_cont(chart, seat_count), nsu_cont(chart, seat_count), nsur_cont(chart, seat_count), nsr_cont(chart, seat_count), nsdr_cont(chart, seat_count), nsd_cont(chart, seat_count), nsdl_cont(chart, seat_count), nsl_cont(chart, seat_count)]
                        nbr_count = 0
                        for nbr in nbrs:
                            check = sd[nbr]
                            # print(f"check: {check}")
                            nbr_count += check

                if seat == 'L' and nbr_count == 0:
                    # print("A")
                    new_sc_row.append('#')
                    changes += 1
                elif seat == '#' and nbr_count >= 5:
                    # print("B")
                    new_sc_row.append('L')
                    changes += 1
                else:
                    # print(f"seat = {seat} --->C")
                    new_sc_row.append(seat)
            
            # print(nbrs)
            seat_num += 1
            seat_count += 1
            nbr_count = 0

        new_sc.append(new_sc_row)
        row_num += 1
    # print(changes)
    return new_sc


sc = []

# imports the seat map
with open('input') as input_file:
    for line in input_file:
        sc.append(line.rstrip())

for i in range(len(sc)):
    new_line = sc.pop(0)
    split_line = []
    for j in range(len(new_line)):
        split_line.append(new_line[j])
    sc.append(split_line)

    
counter = 0
keep_shuffling = True

# calls the chuffle function to create a new seat map, and doesn't stop until it eaches
# a steady state.  Currently limits to 500 iterations to prevent an infinite loop.
while counter < 500 and keep_shuffling == True:


    counter+= 1
    new_sc = shuffle_seats(sc)
    print("SHUFFLED") # for debugging only
    if new_sc == sc:
        
        seats_occ = 0
        keep_shuffling = False
        for line in new_sc:
            #print(line)
            for seat in line:
                if seat == "#":
                    seats_occ += 1
        
        # this prints the answer to the question.
        print(f"{seats_occ} seats are occupied after {counter} rounds of shuffling.")

    
    sc = shuffle_seats(sc)

    # to monitor progress in the console.
    print(f"COUNTER*************{counter}")


        
    
