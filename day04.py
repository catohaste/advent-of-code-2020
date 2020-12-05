import numpy as np

f = open("day04_input.txt", "r")

entries = []
entry = ''
for line in f:
    line = line[:-1]
    if line != '':
        entry = entry + ' ' +line
    elif line == '':
        entry = entry[1:]
        entries.append(entry)
        entry = ''
    
fields = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']

valid = 0
for entry in entries:
    count = 0
    for field in fields:
        if field in entry:
            count += 1
    if count == 7:
        valid += 1

print(valid)


valid = 0
for entry in entries:
    count = 0
    for field in fields:
        if field in entry:
            count += 1
    if count == 7:
        byr = int(entry.split('byr:')[1].split(' ')[0])
        iyr = int(entry.split('iyr:')[1].split(' ')[0])
        eyr = int(entry.split('eyr:')[1].split(' ')[0])
        hgt = entry.split('hgt:')[1].split(' ')[0]
        hcl = entry.split('hcl:')[1].split(' ')[0]
        ecl = entry.split('ecl:')[1].split(' ')[0]
        pid = entry.split('pid:')[1].split(' ')[0]
        
        hgt_valid = False
        if hgt[-2:] == 'in':
            hgt_int = int(hgt[:-2])
            hgt_valid =  (hgt_int >= 59) and (hgt_int <= 76)
        elif hgt[-2:] == 'cm':
            hgt_int = int(hgt[:-2])
            hgt_valid = (hgt_int >= 150) and (hgt_int <= 193)
        
        hcl_valid = False
        if len(hcl) == 7 and (hcl[0] == '#'):
            hcl_valid = True
        
        ecl_options = ['amb','blu','brn','gry','grn','hzl','oth']
        pid_valid = False
        if len(pid) == 9:
            pid_valid = True
            
        if byr >= 1920 and byr <= 2002 and iyr >= 2010 and iyr <= 2020 and eyr >= 2020 and eyr <= 2030 and hgt_valid and hcl_valid and (ecl in ecl_options) and pid_valid:
                valid += 1

print(valid)
    



