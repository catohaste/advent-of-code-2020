from copy import deepcopy

f = open("day05_input.txt", "r")

codes = []
for line in f:
    line = line[:-1]
    codes.append(line)
    
# print(codes)

rows = list(range(128))
cols = list(range(8))

seatIDs = []

for code in codes:

    sub_rows = deepcopy(rows)
    sub_cols = deepcopy(cols)

    row_code = code[:7]
    col_code = code[-3:]

    current_row_index = 0
    while current_row_index < 7:
        current_row_length = len(sub_rows)
        if row_code[current_row_index] == 'F':
            sub_rows = sub_rows[0:int(current_row_length/2)]
        elif row_code[current_row_index] == 'B':
            sub_rows = sub_rows[int(current_row_length/2):]
        current_row_index += 1

    current_col_index = 0
    while current_col_index < 3:
        current_col_length = len(sub_cols)
        if col_code[current_col_index] == 'L':
            sub_cols = sub_cols[0:int(current_col_length/2)]
        elif col_code[current_col_index] == 'R':
            sub_cols = sub_cols[int(current_col_length/2):]
        current_col_index += 1

    seatID = sub_rows[0] * 8 + sub_cols[0]
    
    seatIDs.append(seatID)
    
print(max(seatIDs))

for possible in range(max(seatIDs)):
    if possible not in seatIDs:
        print(possible)

