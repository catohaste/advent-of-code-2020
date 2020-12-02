import numpy as np

class passwordEntry:
    
    def __init__(self, input_string):
        
        rule, password = input_string.split(': ')
        self.password = password[:-1]
        
        self.test_letter = rule[-1]
        
        self.lower = int(rule.split('-')[0])
        
        self.upper = int(rule.split('-')[1].split(' ')[0])
        
    def test_password(self):
        
        return self.password.count(self.test_letter) >= self.lower and self.password.count(self.test_letter) <= self.upper
        
    def test_password2(self):
        
        return (self.password[self.lower - 1] == self.test_letter) != (self.password[self.upper - 1] == self.test_letter)

f = open("day02_input.txt", "r")
passwords = []

for x in f:
    passwords.append(passwordEntry(x))

count = 0
count2 = 0
for password in passwords:
    if password.test_password():
        count += 1
    if password.test_password2():
        count2 += 1
        
print(count) 
print(count2)
        