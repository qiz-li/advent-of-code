# Find this puzzle at:
# https://adventofcode.com/2020/day/4

import re
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n\n')]
valid = 0
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
# Put each passport into a dictionary
for person in puzzle_input:
    dct = dict(i.split(':') for i in person.split())
    try:
        # Validation of items
        # Unsure if this is best practice
        if (len(dct.get('byr')) == len(dct.get('iyr')) == len(dct.get('eyr'))
           == 4 and 1920 <= int(dct.get('byr')) <= 2002 and 2010 <=
           int(dct.get('iyr')) <= 2020 and 2020 <= int(dct.get('eyr'))
           <= 2030 and (dct.get('hgt')[-2:] == 'cm' and 150 <=
           int(dct.get('hgt')[:-2]) <= 193 or dct.get('hgt')[-2:] == 'in'
           and 59 <= int(dct.get('hgt')[:-2]) <= 76) and dct.get('ecl')
           in eye_colors and dct.get('hcl')[:1] == '#'
           and re.search(r'[a-fA-F0-9]', dct.get('hcl')[1:])
           and len(dct.get('hcl')[1:]) == 6 and len(dct.get('pid')) == 9
           and dct.get('pid').isnumeric()):
            valid += 1
    except TypeError:
        pass
print(valid)
