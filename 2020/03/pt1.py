# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i.strip('\n') for i in file.readlines()]
idx = tree = 0
# With each line (down 1) the index +3 (right 3)
for line in puzzle_input[1:]:
    idx += 3
    # If index extends out of the list, start counting from beginning.
    if idx > len(line) - 1:
        idx -= len(line)
    if line[idx] == "#":
        tree += 1
print(tree)
