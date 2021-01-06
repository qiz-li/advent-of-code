# Find this puzzle at:
# https://adventofcode.com/2020/day/8

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
complete = set()
tried = set()
idx = acc = 0
trying = 0
# Only continue if all the operations did not execute properly
while idx != len(puzzle_input):
    operation, argument = puzzle_input[idx].split()
    argument = int(argument)
    operation_id = operation + str(idx)
    # Check first if this operation is already in the "complete" set.
    # If so, the program fails because it is an infinite loop,
    # so we rest everything and try again.
    if operation_id in complete:
        complete = set()
        acc = idx = 0
        tried.add(trying)
        trying = 0
        continue
    complete.add(operation_id)
    # acc operations excute normally
    if operation == 'acc':
        acc += argument
    # If a nop operation has never been tried before,
    # it changes to a jmp operation and is added to the "tried" set.
    elif operation == 'nop' and not trying and operation_id not in tried:
        trying = operation_id
        operation = 'jmp'
    if operation == 'jmp':
        # If a jmp operation has never been tried before,
        # it is added to the "tried" set and
        # changes to a nop operation by doing nothing.
        if not trying and operation_id not in tried:
            trying = operation_id
        else:
            idx += argument - 1
    idx += 1
print(acc)
