# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n')]
bags = {'shiny gold'}
# Has to loop through multiple times to get all the bags
for check in puzzle_input:
    bags_last = len(bags)
    for rule in puzzle_input:
        # Splits each rule into a list of bags
        for i in ('s contain', '.', 's, ', ', ',):
            rule = rule.replace(i, '')
        bag_lst = list(rule.split(' bag'))
        bag_lst.pop()
        # If any of the "subbags" is a bag containing shiny gold,
        # add the "masterbag" to the list
        for bag in bag_lst[1:]:
            bag = ''.join([i for i in bag if not i.isnumeric()])
            if bag.strip() in bags:
                bags.add(bag_lst[0])
                break
    # If the list doesn't change, all the bags have been found
    if bags_last == len(bags):
        break
print(len(bags) - 1)
