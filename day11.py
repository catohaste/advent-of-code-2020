import numpy as np
from copy import deepcopy

f = open("day11_input.txt", "r")

grid = []

for line in f:
    line = line[:-1]
    grid.append(line)

# print(grid)

rowN = len(grid)
colN = len(grid[0])

new_grid = np.ndarray((rowN,colN),dtype=int)
for row_idx, row in enumerate(grid):
    for seat_idx, seat in enumerate(row):
        if grid[row_idx][seat_idx] == '.':
            new_grid[row_idx,seat_idx] = 0
        elif grid[row_idx][seat_idx] == 'L':
            new_grid[row_idx,seat_idx] = 1
        elif grid[row_idx][seat_idx] == '#':
            new_grid[row_idx,seat_idx] = 2
        else:
            print('Something went wrong')
            
old_grid = np.ndarray((rowN,colN),dtype=int)

# print(old_grid)
# print(new_grid)
# reps = [0,1,2,3,4]
#
# while not (new_grid == old_grid).all():
# # for rep in reps:
#     old_grid = deepcopy(new_grid)
#
#     for row_idx in range(rowN):
#         for seat_idx in range(colN):
#             current_seat = old_grid[row_idx,seat_idx]
#             # print(current_seat)
#             if current_seat == 0:
#                 new_grid[row_idx,seat_idx] = 0
#                 continue
#
#             """ define neighbours"""
#             if row_idx - 1 < 0:
#                 row_neighbours = [row_idx, row_idx + 1]
#             elif row_idx + 1 == rowN:
#                 row_neighbours = [row_idx - 1, row_idx]
#             else:
#                 row_neighbours = [row_idx - 1, row_idx, row_idx + 1]
#
#             if seat_idx - 1 < 0:
#                 col_neighbours = [seat_idx, seat_idx + 1]
#             elif seat_idx + 1 == colN:
#                 col_neighbours = [seat_idx - 1, seat_idx]
#             else:
#                 col_neighbours = [seat_idx - 1, seat_idx, seat_idx + 1]
#
#             # print(row_neighbours, col_neighbours)
#             neighbours = []
#             for i in row_neighbours:
#                 for j in col_neighbours:
#                     neighbours.append((i,j))
#             neighbours.remove((row_idx, seat_idx))
#             # print(neighbours)
#
#             """ test neighbours """
#             if current_seat == 1:
#                 empty_neighbours = []
#                 for neighbour in neighbours:
#                     if ((old_grid[neighbour[0],neighbour[1]] == 1) or (old_grid[neighbour[0], neighbour[1]] == 0)):
#                         empty_neighbours.append(True)
#                     else:
#                         empty_neighbours.append(False)
#                 if all(empty_neighbours):
#                     new_grid[row_idx,seat_idx] = 2
#
#             elif current_seat == 2:
#                 occupied_neighbours = [True for neighbour in neighbours if old_grid[neighbour[0], neighbour[1]] == 2]
#                 # print(occupied_neighbours.count(True))
#                 if occupied_neighbours.count(True) >= 4:
#                     new_grid[row_idx,seat_idx] = 1
#
#
# # print(not (new_grid == old_grid).all())
# # print(old_grid)
# # print(new_grid)
#
# unique, counts = np.unique(new_grid, return_counts=True)
# answer_dict = dict(zip(unique, counts))
# print(answer_dict[2])

##############################################################################



# print(old_grid)
# print(new_grid)
reps = [0,1]

while not (new_grid == old_grid).all():
# for rep in reps:
    old_grid = deepcopy(new_grid)

    for row_idx in range(rowN):
        for seat_idx in range(colN):
            current_seat = old_grid[row_idx,seat_idx]
            # print(current_seat)
            if current_seat == 0:
                new_grid[row_idx,seat_idx] = 0
                continue
                
            """ define neighbours"""
            vectors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            neighbours = []
            for vector in vectors:
                neighbour_pos = (row_idx,seat_idx)
                neighbour_pos = np.add(neighbour_pos,vector)
                while 0 <= neighbour_pos[0] < rowN and 0 <= neighbour_pos[1] < colN:
                    # print(neighbour_pos,vector)
                    if old_grid[neighbour_pos[0],neighbour_pos[1]] in (1,2):
                        neighbours.append(neighbour_pos)
                        break
                    neighbour_pos = np.add(neighbour_pos,vector)
            # print(neighbours)
    
            """ test neighbours """
            if current_seat == 1:
                empty_neighbours = []
                for neighbour in neighbours:
                    if ((old_grid[neighbour[0],neighbour[1]] == 1) or (old_grid[neighbour[0], neighbour[1]] == 0)):
                        empty_neighbours.append(True)
                    else:
                        empty_neighbours.append(False)
                if all(empty_neighbours):
                    new_grid[row_idx,seat_idx] = 2

            elif current_seat == 2:
                occupied_neighbours = [True for neighbour in neighbours if old_grid[neighbour[0], neighbour[1]] == 2]
                # print(occupied_neighbours.count(True))
                if occupied_neighbours.count(True) >= 5:
                    new_grid[row_idx,seat_idx] = 1


# print(not (new_grid == old_grid).all())
# print(old_grid)
# print(new_grid)

unique, counts = np.unique(new_grid, return_counts=True)
answer_dict = dict(zip(unique, counts))
print(answer_dict[2])

        