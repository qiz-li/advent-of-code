# Find this puzzle at:
# https://adventofcode.com/2020/day/7

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
bags = {}
# Go until we have "shiny gold" bag amount
while 'shiny gold' not in bags:
    for rule in puzzle_input:
        # No need to keep on going if we already have "shiny gold" bag amount
        if 'shiny gold' in bags:
            break
        valid_bags = total_contained = 0
        # Splits each rule into a list of bags
        for i in ('s contain', '.', 's, ', ', ',):
            rule = rule.replace(i, '')
        bag_lst = list(rule.split(' bag'))
        bag_lst.pop()
        for bag in bag_lst[1:]:
            bag_no_num = ''.join([i for i in bag if not i.isdigit()])
            # If the bag contains "no other" bags,
            # only add the bag itself (value 1)
            if bag_no_num.strip() == "no other":
                bags[bag_lst[0]] = 1
                break
            # Calculate the amount of contained bags,
            # this is done by multiplying each bag's amount
            # by the amount of bags inside that bag
            elif bag_no_num.strip() in bags:
                valid_bags += 1
                bag_amount = int(''.join([i for i in bag if i.isdigit()]))
                total_contained += bag_amount * bags.get(bag_no_num.strip())
        # If all sub-bags of the main-bag are in the known list,
        # meaning we know the total amount of bags inside the main-bag,
        # add the sub-bag and the total amount of bags inside it to the list
        if valid_bags + 1 == len(bag_lst):
            bags[bag_lst[0]] = total_contained + 1
print(bags.get('shiny gold') - 1)
