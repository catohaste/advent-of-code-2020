import numpy as np
from copy import deepcopy

f = open("day08_input.txt", "r")

rules = []

for line in f:
    line = line[:-1]
    rules.append(line)
    
# print(rules[-1])

exec_order = []
acc = 0
acc_log = [0]

current_exec_index = 0
while len(exec_order) == len(set(exec_order)):

    rule = rules[current_exec_index]

    action = rule.split(' ')[0]
    count = int(rule.split(' ')[1])

    if action == 'nop':
        current_exec_index += 1
    elif action == 'acc':
        current_exec_index += 1
        acc += count
    elif action == 'jmp':
        current_exec_index += count
        
    if current_exec_index == len(rules):
        break
        
    exec_order.append(current_exec_index)
    acc_log.append(acc)
    
    # print(rule, current_exec_index, acc)

print(acc_log[-1])




for idx in range(len(rules)):
    rule = rules[idx]
    action = rule.split(' ')[0]
    count_str = rule.split(' ')[1]
    count = int(rule.split(' ')[1])
    
    ''' change rule '''
    if action == 'acc':
        continue
    elif action == 'nop':
        rules[idx] = 'jmp ' + count_str
    elif action == 'jmp':
        rules[idx] = 'nop ' + count_str
        
    exec_order = []
    acc = 0
    acc_log = [0]
    
    # print(rules)

    current_exec_index = 0
    while len(exec_order) == len(set(exec_order)):

        while_rule = rules[current_exec_index]

        while_action = while_rule.split(' ')[0]
        while_count = int(while_rule.split(' ')[1])

        if while_action == 'nop':
            current_exec_index += 1
        elif while_action == 'acc':
            current_exec_index += 1
            acc += while_count
        elif while_action == 'jmp':
            current_exec_index += while_count

        if current_exec_index == len(rules):
            break

        exec_order.append(current_exec_index)
        acc_log.append(acc)
    
    if current_exec_index == len(rules):
        break
    
    ''' change rule back '''
    if action == 'nop':
        rules[idx] = 'nop ' + count_str
    elif action == 'jmp':
        rules[idx] = 'jmp ' + count_str

print(acc)
