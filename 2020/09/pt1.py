# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n')]
idx = 25
while True:
    # Loop through all 25 numbers before the number.
    # If two of them add up to the number, break.
    for number in puzzle_input[idx - 25:idx]:
        if (str(int(puzzle_input[idx]) - int(number))
           in puzzle_input[idx - 25:idx]):
            idx += 1
            break
    # Else no numbers add up and we have found the answer
    else:
        print(puzzle_input[idx])
        break
