# Find this puzzle at:
# https://adventofcode.com/2020/day/13

with open('input.txt', 'r') as file:
    puzzle_input = file.readlines()[1].split(',')
print(puzzle_input)
time = 1
difference = int(puzzle_input[0])
initial = 0
number = 0
idx = 0
while idx < len(puzzle_input):
    number += difference
    print(number)
    while idx < len(puzzle_input):
        if puzzle_input[idx] != 'x':
            if number % int(puzzle_input[idx]) == 0:
                if idx == len(puzzle_input) - 1:
                    print(number - len(puzzle_input) + 1)
                    idx += 1000
                    break
                print(number, idx, len(puzzle_input))
                initial = number
                while idx < len(puzzle_input):
                    number += difference
                    print(number)
                    if number % int(puzzle_input[idx]) == 0:
                        difference = number - initial
                        print(difference)
                        break
                number = initial
                number += 1
                idx += 1
            else:
                print(number, difference)
                break
        else:
            number += 1
            idx += 1
            print(number)

# print(number - len(puzzle_input))
# bus_lst = [7, 13, 59, 31, 19]
# lst = [1068781, 1068782, 1068785, 1068787, 1068788]
# som = 0
# bus_som = 0
# for i in lst:
#     som += i
# for i in bus_lst:
#     bus_som += 1

# print((som-len(bus_lst)))

# while True:
#     number = int(puzzle_input[0]) * time
#     for bus in puzzle_input:
#         if bus != 'x':
#             if number % int(bus) == 0:
#                 number += 1
#             else:
#                 break
#         else:
#             number += 1
#     else:
#         break
#     time += 1
# print(number - len(puzzle_input))
# number = 187727
# for i in range(4):
#     while True:
#         number = 6637309354 + (6637309354 - 1818642371) * time
#         time += 1
#         if (not (number + 31) % 983 and not (number - 41) % 41
#            and not (number + 13) % 13 and not (number + 17) % 17
#            and not (number - 6) % 37 and not (number + 8) % 23
#            and not (number + 29) % 29 and not (number + 50) % 19):
#             print(number - 41)
#             break
    

    #  
    #        and not (number + 11) % 13 and not (number + 14) % 17
    #        and not (number - 5) % 37 and not (number + 7) % 23
    #        and not (number + 25) % 29 and not (number + 44) % 19


            # and not (number + 11) % 13
        #  and
        #    not (number + 11) % 13 and not (number + 14) % 17
        # not number % 541 and not (number - 39) % 41 and
        #    not (number - 5) % 37 and not (number + 7) % 23
        # and not (number - 39) % 41 and
        #    not (number - 5) % 37 and not (number + 7) % 23)

# 1484237828841757
# 3743715595837440
# 6003193362833123
# 8262671129828806