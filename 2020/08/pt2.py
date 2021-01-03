# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n')]
complete = set()
tried = set()
acc = idx = 0
trying = ""
# Only continue if all the operations did not execute properly.
while idx != len(puzzle_input):
    operation, argument = puzzle_input[idx].split()
    # Check first if this operation is already in the "complete" set.
    # If so, the program fails because it is an infinite loop,
    # so we rest everything and try again.
    if operation + str(idx) in complete:
        complete = set()
        acc = idx = 0
        tried.add(trying)
        trying = ""
        operation, argument = puzzle_input[idx].split()
    complete.add(operation + str(idx))
    # acc operations excute normally
    if operation == 'acc':
        if argument[0] == '+':
            acc += int(argument[1:])
        elif argument[0] == '-':
            acc -= int(argument[1:])
    # If a nop operation has never been tried before,
    # it changes to a jmp operation and is added to the "tried" set.
    elif (operation == 'nop' and len(trying) == 0
          and operation + str(idx) not in tried):
        trying = operation + str(idx)
        operation = 'jmp'
    elif operation == 'jmp':
        # If a jmp operation has never been tried before,
        # it is added to the "tried" set and
        # changes to a nop operation by doing nothing.
        if len(trying) == 0 and operation + str(idx) not in tried:
            trying = operation + str(idx)
        elif argument[0] == '+':
            idx += int(argument[1:]) - 1
        elif argument[0] == '-':
            idx -= (int(argument[1:]) + 1)
    idx += 1
print(acc)
