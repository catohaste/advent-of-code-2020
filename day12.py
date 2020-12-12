import numpy as np
from copy import deepcopy

f = open("day12_input.txt", "r")

directions = []

for line in f:
    line = line[:-1]
    directions.append(line)
    
# print(directions)

facing = 0      # degrees in cartesian coordinates, 0 = E
position = [0,0]

for direction in directions:
    facing = facing % 360
    temp_direction = None
    if direction[0] is 'F':
        if facing == 0:
            temp_direction = 'E' + direction[1:]
        elif facing == 90:
            temp_direction = 'N' + direction[1:]
        elif facing == 180:
            temp_direction = 'W' + direction[1:]
        elif facing == 270:
            temp_direction = 'S' + direction[1:]
    else:
        temp_direction = deepcopy(direction)

    if temp_direction[0] is 'N':
        position[1] += int(temp_direction[1:])
    elif temp_direction[0] is 'S':
        position[1] -= int(temp_direction[1:])
    elif temp_direction[0] is 'E':
        position[0] += int(temp_direction[1:])
    elif temp_direction[0] is 'W':
        position[0] -= int(temp_direction[1:])
    elif temp_direction[0] is 'L':
        facing += int(temp_direction[1:])
    elif temp_direction[0] is 'R':
        facing -= int(temp_direction[1:])
        
    # print(position, facing)
        
# print(position)

print(np.abs(position[0]) + np.abs(position[1]))

####################################################################################

position = [0,0]
waypoint = [10,1]

for direction in directions:

    if direction[0] is 'N':
        waypoint[1] += int(direction[1:])
    elif direction[0] is 'S':
        waypoint[1] -= int(direction[1:])
    elif direction[0] is 'E':
        waypoint[0] += int(direction[1:])
    elif direction[0] is 'W':
        waypoint[0] -= int(direction[1:])
    elif direction[0] is 'F':
        position = np.add(position, [x * int(direction[1:]) for x in waypoint])
    elif direction[0] == 'L' or direction[0] == 'R':
        if direction[1:] == '180':
            waypoint = [-waypoint[0],-waypoint[1]]
        elif direction == 'R270' or direction == 'L90':
            waypoint = [-waypoint[1], waypoint[0]]
        elif direction == 'L270' or direction == 'R90':
            waypoint = [waypoint[1],-waypoint[0]]
                
    # print(position, waypoint)
        
# print(position)

print(np.abs(position[0]) + np.abs(position[1]))
