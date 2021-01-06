# Find this puzzle at:
# https://adventofcode.com/2020/day/7

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
bags = {'shiny gold'}
bags_last = 0
# If the list doesn't change, all bags have been found.
while bags_last != len(bags):
    bags_last = len(bags)
    for rule in puzzle_input:
        # Splits each rule into a list of bags
        for i in ('s contain', '.', 's, ', ', ',):
            rule = rule.replace(i, '')
        bag_lst = list(rule.split(' bag'))
        bag_lst.pop()
        # If any of the sub-bags are in the "bags" list,
        # meaning it contains shiny gold;
        # add the main-bag to the "bags" list.
        for bag in bag_lst[1:]:
            bag = ''.join([i for i in bag if not i.isnumeric()])
            if bag.strip() in bags:
                bags.add(bag_lst[0])
                break
print(len(bags) - 1)
