import numpy as np
from copy import deepcopy

f = open("day07_input.txt", "r")

rules = []

for line in f:
    line = line[:-1]
    rules.append(line)
    
# print(rules)

all_bags = set([])
new_additions = set(['shiny gold bag'])

while len(new_additions) != 0:
    all_bags = all_bags.union(new_additions)
    search_items = deepcopy(new_additions)
    new_additions = set([])
    for search_item in search_items:
        for rule in rules:
            start_rule = rule.split('contain')[0][:-2]
            end_rule = rule.split('contain')[1]
            if search_item in end_rule:
                new_additions = new_additions.union(set([start_rule]))

# print(all_bags)
all_bags.remove('shiny gold bag')
print(len(all_bags))



dead_end_bags = []
known_bags = {}
for rule in rules:
    start_rule = rule.split('contain ')[0][:-2]
    if 'no' in rule:
        dead_end_bags.append(start_rule)
        known_bags[start_rule] = 0
# print(known_bags)

while 'shiny gold bag' not in known_bags:
    for rule in rules:
        start_rule = rule.split('contain ')[0][:-2]
        if start_rule in known_bags:
            continue
        end_rule = rule.split('contain ')[1]
        bags = end_rule.split(', ')
        bags[-1] = bags[-1][:-1]
        edited_bags = []
        counts = []
        for bag in bags:
            count = bag.split(' ')[0]
            if count == 'no':
                count = 0
            count = int(count)
            counts.append(count)
        
            bag_word_list = bag.split(' ')[1:]
            new_bag = ''
            for word in bag_word_list:
                new_bag += word + ' '
            if count == 1:
                new_bag = new_bag[:-1]
            elif count > 1:
                new_bag = new_bag[:-2]
            edited_bags.append(new_bag)
    
        if set(edited_bags).issubset(set(known_bags.keys())):
            # print(start_rule, edited_bags)
            level_below_counts = []
            for bag in edited_bags:
                 level_below_counts.append(known_bags[bag])
            # print(counts,level_below_counts)
            known_bags[start_rule] = sum(counts) + np.sum(np.multiply(counts,level_below_counts))

        
print(known_bags['shiny gold bag'])
            

