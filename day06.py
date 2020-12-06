import numpy as np

f = open("day06_input.txt", "r")

responses = []
unique_responses = []
response = ''
response_spaced = ''
for line in f:
    line = line[:-1]
    if line != '':
        response = response + line
        response_spaced = response_spaced + " " + line
    elif line == '':
        response_spaced = response_spaced[1:]
        responses.append(response_spaced)
        unique_responses.append(set(response))
        response = ''
        response_spaced = ''

sum = 0
for response in unique_responses:
    sum += len(response)
    
print(sum)

answers = []
for a in responses:

    split_response = a.split(' ')
    # print(split_response)
    
    split_sets = [set(b) for b in split_response]
    # print(split_sets)

    if len(split_sets) == 1:
        answer = split_sets[0]
    elif len(split_sets) == 2:
        answer = split_sets[0] & split_sets[1]
    else:
        answer = split_sets[0] & split_sets[1]
        for c in split_sets[2:]:
            answer = answer & c
    
    # print(answer,len(answer))
    answers.append(answer)


sum = 0
for d in answers:
    sum += len(d)
    
print(sum)
    

