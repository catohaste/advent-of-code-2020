import numpy as np
from copy import deepcopy

f = open("day10_input.txt", "r")

adapters = []

for line in f:
    line = line[:-1]
    adapters.append(int(line))
    
adapters.sort()

differences = []
for idx in range(1,len(adapters)):
    differences.append(adapters[idx] - adapters[idx-1])

ones = differences.count(1)
threes = differences.count(3)

print((ones + 1) * (threes + 1))


adapters.append(0)
adapters.sort()

count_ways = {}
for adapter in adapters:
    count_ways[adapter] = 0
    
count_ways[0] = 1
# print(count_ways)

for idx in range(1,len(adapters)):
    origin_options = list(range(adapters[idx] - 3, adapters[idx]))
    ok_origins = [option for option in origin_options if option in adapters]

    # print(adapters[idx], origin_options, ok_origins)
    for origin in ok_origins:
        count_ways[adapters[idx]] += count_ways[origin]
    
print(count_ways[adapters[-1]])
    