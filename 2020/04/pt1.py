# Find this puzzle at:
# https://adventofcode.com/2020/day/4

with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n\n')]
valid = 0
required_items = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# Put each passport into a dictionary
for person in puzzle_input:
    dct = dict(i.split(':') for i in person.split())
    # Check if required items are all in dictionary
    if all(item in dct for item in required_items):
        valid += 1
print(valid)
