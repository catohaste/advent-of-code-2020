import numpy as np

input_array = np.loadtxt("day01_input.txt", dtype='float', delimiter='\n')

sorted_array = np.sort(input_array)

for idx, num in enumerate(sorted_array):
    for new_idx in range(idx + 1, len(sorted_array)):
        num_sum = num
        num_sum += input_array[new_idx]
        if num_sum == 2020:
            answer = [num, input_array[new_idx]]
            break
    else:
        continue
    break
            
print(np.product(answer))

for idx, num in enumerate(sorted_array):
    for new_idx in range(idx + 1, len(sorted_array)):
        for newest_idx in range(new_idx + 1, len(sorted_array)):
            num_sum = num + input_array[new_idx] + input_array[newest_idx]
            if num_sum == 2020:
                answer = [num, input_array[new_idx], input_array[newest_idx]]
                break
        else:
            continue
        break
    else:
        continue    
    break
    
print(np.product(answer))

