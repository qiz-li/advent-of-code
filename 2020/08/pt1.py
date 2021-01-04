# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n')]
complete = set()
acc = idx = 0
for line in puzzle_input:
    operation, argument = puzzle_input[idx].split()
    argument = int(argument)
    operation_id = operation + str(idx)
    # Check first if this operation is already in the "complete" set.
    # If so, we have found the infinite loop.
    if operation_id in complete:
        print(acc)
        break
    # If not, execute the operation and add it to the "complete" set
    elif operation == 'acc':
        acc += argument
    elif operation == 'jmp':
        idx += argument - 1
    complete.add(operation_id)
    idx += 1
