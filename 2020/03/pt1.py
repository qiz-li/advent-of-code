# Find this puzzle at:
# https://adventofcode.com/2020/day/3

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
idx = tree = 0
# With each line (down 1) the index +3 (right 3)
for line in puzzle_input[1:]:
    idx += 3
    # If index extends out of the list, start counting from beginning.
    if idx >= len(line):
        idx -= len(line)
    if line[idx] == "#":
        tree += 1
print(tree)
