# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i.strip('\n') for i in file.readlines()]
for number in puzzle_input:
    for number2 in puzzle_input:
        # 2020 minus any two entries is in the list
        if str(2020-int(number)-int(number2)) in puzzle_input:
            # Continue if one entry is being used twice
            if (len([number, number2, str(2020-int(number)-int(number2))]) !=
               len(set([number, number2, str(2020-int(number)-int(number2))]))
               and puzzle_input.count(number) + puzzle_input.count(number2) ==
               2):
                continue
            # Else we've found the answer
            else:
                print(int(number)*int(number2)*(2020-int(number)-int(number2)))
                break
    else:
        continue
    break
