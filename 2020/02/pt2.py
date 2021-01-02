# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i.strip('\n') for i in file.readlines()]
valid = 0
for line in puzzle_input:
    # Extract the indexes, letter, and password
    indexes, letter, password = line.split()
    index_low, index_hi = indexes.split('-')
    # Check if occurance of letter is on either index
    if (password[int(index_low)-1] == letter[0] and password[int(index_hi)-1]
       != letter[0] or password[int(index_low)-1] != letter[0] and password
       [int(index_hi)-1] == letter[0]):
        valid += 1
print(valid)
