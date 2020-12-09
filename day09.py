import numpy as np
from copy import deepcopy

f = open("day09_input.txt", "r")

entries = []

for line in f:
    line = line[:-1]
    entries.append(int(line))

# print(entries)
    
preamble_length = 25
for idx in range(preamble_length, len(entries)):
    preamble = entries[idx - preamble_length:idx]
    sums = []
    # print(preamble)
    for a in range(len(preamble)-1):
        for b in range(a + 1,len(preamble)):
            a_b = preamble[a] + preamble[b]
            sums.append(preamble[a] + preamble[b])
            # print(preamble[a] , preamble[b] , a_b)
    # print(sums)
    if entries[idx] not in sums:
        target = entries[idx]
        print(entries[idx],'not valid')
        break
        

for idx in range(len(entries)):
    sum_list = [entries[idx]]
    next_idx = 1
    while sum(sum_list) < target:
        sum_list.append(entries[idx + next_idx])
        next_idx += 1
    if sum(sum_list) == target:
        # print(sum_list, sum(sum_list))
        break

print(np.min(sum_list) + np.max(sum_list))