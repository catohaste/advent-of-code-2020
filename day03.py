import numpy as np

f = open("day03_input.txt", "r")

grid = []
for x in f:
    line = x[:-1]
    grid.append(line)

position = [0,0]
velocity = [1,3]

count = 0
while position[0] < len(grid):
    if grid[position[0]][position[1] % len(grid[1])] == '#':
        count = count + 1
    position = np.add(position,velocity)
print(count)
        
velocities = [[1,1],[1,3],[1,5],[1,7],[2,1]]
counts = np.zeros((len(velocities,)))

for idx,velocity in enumerate(velocities):
    position = [0,0]
    while position[0] < len(grid):
        if grid[position[0]][position[1] % len(grid[1])] == '#':
            counts[idx] += 1
        position = np.add(position,velocity)
        
print(np.product(counts))