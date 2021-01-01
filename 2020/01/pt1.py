# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i.strip('\n') for i in file.readlines()]
# The numbers are 1010 + 1010
if puzzle_input.count("1010") == 2:
    print(1010**2)
else:
    for number in puzzle_input:
        # 2020 minus number is in the list
        if str(2020-int(number)) in puzzle_input:
            print(int(number)*(2020-int(number)))
            break
