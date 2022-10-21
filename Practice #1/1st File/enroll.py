# Zahir Choudhry
#Practice Hack-a-thon

    # num_enrolled: The number of students who are already in the class (0 or positive)
    # num_ seats: Total # of seats in a class (Always positive)
    # num_reserved_remaining: The number of reserved seats remaining (0 or positive)
    # has_reservation: Whether the student has a reservation
    # A student without a reservation can enroll if the course is not full and there is an unreserved seat.
    # However, the reservation doesn't help if the course is already full

def can_enroll(num_enrolled, num_seats, num_reserved_remaining, has_reservation):
    # There are open seats and the reservation are less that enrolled.
    if(num_enrolled < num_seats and (num_enrolled + num_reserved_remaining) < num_seats): 
        return True
    # There are open seats, the reservations are full but the student has a reservation
    elif(num_enrolled < num_seats and has_reservation == True):
        return True
    else: 
        return False

    pass # FIXME

# print(can_enroll(0, 10, 0, False))
# print(can_enroll(10, 10, 0, False))
# print(can_enroll(7, 10, 2, False))
# ALL THREE PASS

# print(can_enroll(8, 10, 2, False))
# print(can_enroll(8, 10, 2, True))
# print(can_enroll(8, 10, 3, True))

# print(can_enroll(10, 10, 3, True))
# print(can_enroll(11, 10, 3, True))
