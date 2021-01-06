# Find this puzzle at:
# https://adventofcode.com/2020/day/2

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
valid = 0
for line in puzzle_input:
    # Extract the limits, letter, and password
    limits, letter, password = line.split()
    limit_low, limit_hi = limits.split('-')
    # Check if occurance of letter is within limits
    if (password.count(letter[0]) >= int(limit_low) and password.count(letter
       [0]) <= int(limit_hi)):
        valid += 1
print(valid)
