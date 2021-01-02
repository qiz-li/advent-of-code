# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n')]
complete = set()
acc = idx = 0
for line in puzzle_input:
    operation, argument = puzzle_input[idx].split()
    # Check first if this operation is already in the "complete" set.
    # If so, we have found the infinite loop.
    if operation + str(idx) in complete:
        break
    # If not, execute the operation and add it to the "complete" set
    elif operation == 'acc':
        if argument[0] == '+':
            acc += int(argument[1:])
        elif argument[0] == '-':
            acc -= int(argument[1:])
    elif operation == 'jmp':
        if argument[0] == '+':
            idx += int(argument[1:]) - 1
        elif argument[0] == '-':
            idx -= (int(argument[1:]) + 1)
    complete.add(operation + str(idx))
    idx += 1
print(acc)
