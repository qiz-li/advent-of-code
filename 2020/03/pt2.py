# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i.strip('\n') for i in file.readlines()]
# List of slopes to test [right, down]
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree_total = 1
for slope in slopes:
    right, down = slope
    idx = tree = 0
    # Row goes down by the specified amount,
    # and each time index increase by specified amount.
    for line in puzzle_input[down::down]:
        idx += right
        # If index extends out of the list, start counting from beginning.
        if idx > len(line) - 1:
            idx -= len(line)
        if line[idx] == "#":
            tree += 1
    tree_total *= tree
print(tree_total)
