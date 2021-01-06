# Find this puzzle at:
# https://adventofcode.com/2020/day/10
# This one took a while, phew!!

with open('input.txt', 'r') as file:
    puzzle_input = [int(i) for i in file.read().splitlines()]
# Add the charging outlet (0) to the list, no need to add the built-in adopter
# because + 3 cannot have different arrangements anyway
# (e.g. 6, 7, 10, we have to use 7 to get to 10;
# there are no other possible arrangements).
puzzle_input.append(0)
puzzle_input.sort()
arrangements = 1
prev_arrangements = []
# Because of how the arrangments relay on top of each other,
# the possible arrangements of a number is actually the sum
# of possibles arrangments of previous numbers.
for idx, adapter in enumerate(puzzle_input):
    # If the previous numbers of the nth number are n-1, n-2, n-3,
    # respectively. The possible arrangements of n is the sum of
    # the possible arrangements of n-1, n-2, n-3, the previous three
    # numbers of n. This, in short, is because since all of them are
    # connected to n, they port over their possible arrangements.
    if all(i in puzzle_input for i in [adapter - 1, adapter - 2, adapter - 3]):
        arrangements = sum(prev_arrangements[-3:])
    # Following the rule above, if there are only two previous numbers
    # connected to n (e.g. n-1 and n-3), the possible
    # arangements of those two previous numbers are ported over.
    elif (len([i for i in [adapter - 1, adapter - 2,
          adapter - 3] if i in puzzle_input]) == 2):
        arrangements = sum(prev_arrangements[-2:])
    # If only one previous number connects to n,
    # then really nothing changes.Only the possible arrangement
    # of that number is ported over, remaining the same.
    prev_arrangements.append(arrangements)
print(arrangements)
