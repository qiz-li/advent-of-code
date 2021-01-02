# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n')]
for idx in range(len(puzzle_input)):
    numbers_sum = 0
    numbers_lst = []
    # Try each number in the list
    for num_try in puzzle_input:
        # The value of the first number and
        # each number after the first is added to the "numbers sum"
        numbers_sum += int(puzzle_input[idx])
        numbers_lst.append(int(puzzle_input[idx]))
        idx += 1
        # We have found our list of numbers, break.
        if numbers_sum == 167829540 and len(numbers_lst) != 1:
            numbers_lst.sort()
            print(numbers_lst[0] + numbers_lst[-1])
            break
        # No need to keep on adding if the sum is above our number
        elif numbers_sum > 167829540:
            break
    # We have found our list of numbers, no need to keep on looping.
    if numbers_sum == 167829540 and len(numbers_lst) != 1:
        break
