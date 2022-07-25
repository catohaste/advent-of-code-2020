import numpy as np
from copy import deepcopy

f = open("day13_input.txt", "r")

data = []

for line in f:
    line = line[:-1]
    data.append(line)
    
depart_time = int(data[0])
# print(depart_time)

bus_IDs = data[1].split(',')
# print(bus_IDs)

# bus_IDs = ['17','x','13','19']
# bus_IDs = ['67','7','59','61']
# bus_IDs = ['67','x','7','59','61']
# bus_IDs = ['67','7','x','59','61']
# bus_IDs = ['1789','37','47','1889']

valid_bus_IDs = [int(x) for x in bus_IDs if x is not 'x']
# print(valid_bus_IDs)

wait_times = [bus_ID - (depart_time % bus_ID) for bus_ID in valid_bus_IDs]
# print(wait_times)

answer = valid_bus_IDs[wait_times.index(min(wait_times))] * min(wait_times)
# print(answer)


################################################################################################
""" This would work given enough time """

bus_offset_tuples = [(bus_ID, (bus_ID - bus_IDs.index(str(bus_ID))) % bus_ID) for bus_ID in valid_bus_IDs]
offsets = [(bus_ID - bus_IDs.index(str(bus_ID))) % bus_ID for bus_ID in valid_bus_IDs]
# offsets = [bus_IDs.index(str(bus_ID)) % bus_ID for bus_ID in valid_bus_IDs]
# # print(bus_offset_tuples)
#
# max_bus_ID = max(valid_bus_IDs)
# max_ID_offset = max_bus_ID - bus_IDs.index(str(max_bus_ID))
# # print(max_bus_ID, max_ID_offset)
#
# # print(np.product(valid_bus_IDs))
#
# # start_idx = 0
# start_idx = np.floor( 100000000000000 / max_bus_ID)
# end_idx = np.ceil(749468541208439 / max_bus_ID)
# current_idx = deepcopy(start_idx)
# test_list = [False for i in bus_offset_tuples]
# while not all(test_list) and current_idx < end_idx:
#
#     test_list = [False for i in bus_offset_tuples]
#
#     current_idx += 1
#     current_t = current_idx * max_bus_ID + max_ID_offset
#
#     for tuple_idx in range(len(bus_offset_tuples)):
#         current_tuple = bus_offset_tuples[tuple_idx]
#         test_val = (current_t - current_tuple[1]) % current_tuple[0]
#         # print(current_tuple, test_val)
#         if test_val is not 0:
#             break
#         else:
#             test_list[tuple_idx] = True
#
#
# print(current_t)

################################################################################################

def extended_euclid_gcd(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y 
    """
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = np.floor_divide(old_r,r,dtype=np.int_) # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]


solutions = np.zeros((len(valid_bus_IDs),), dtype=np.int_)
solutions[0] = offsets[0]
# print(solutions, type(solutions))
for idx in range(1,len(valid_bus_IDs)):
    
    current_pair = np.zeros((2,), dtype=np.int_)
    current_pair[0] = np.product(valid_bus_IDs[:idx])
    current_pair[1] = valid_bus_IDs[idx]
    # current_pair = (np.product(valid_bus_IDs[:idx]), valid_bus_IDs[idx])
    print(current_pair)
    
    gcd, bezout1, bezout2 = extended_euclid_gcd(current_pair[0], current_pair[1])
    # print(bezout1 * current_pair[0] + bezout2 * current_pair[1])
    
    solution = (bezout1 * current_pair[0] * offsets[idx] + bezout2 * current_pair[1] * solutions[idx-1])    
    solutions[idx] = np.mod(solution , current_pair[0] * current_pair[1])
    
    
print(solutions[-1])
