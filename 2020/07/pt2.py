# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n')]
bags = {}
# Has to loop through multiple times to get all the bags
for check in puzzle_input:
    for rule in puzzle_input:
        # No need to keep on going if we already have 'shiny gold' bag amount
        if 'shiny gold' in bags:
            break
        valid_bags = total_contained = 0
        # Splits each rule into a list of bags
        for i in ('s contain', '.', 's, ', ', ',):
            rule = rule.replace(i, '')
        bag_lst = list(rule.split(' bag'))
        bag_lst.pop()
        # Add how many bags are in the specified bag
        for bag in bag_lst[1:]:
            bag_no_num = ''.join([i for i in bag if not i.isdigit()])
            # If there is "no other" bags contained,
            # only add the bag itself (value 1)
            if bag_no_num.strip() == "no other":
                bags[bag_lst[0]] = 1
                break
            # Calculate the amount of contained bags,
            # this is done by multiplying the each bag's amount
            # by the amount of bags inside that bag
            elif bag_no_num.strip() in bags:
                valid_bags += 1
                bag_amount = int(''.join([i for i in bag if i.isdigit()]))
                total_contained += bag_amount * bags.get(bag_no_num.strip())
        # If both "subbags" are in the known list,
        # meaning we know the total amount of bags inside the "masterbag",
        # add the "masterbag" and its contained bag amount to the list
        if valid_bags + 1 == len(bag_lst):
            bags[bag_lst[0]] = total_contained + 1
    else:
        continue
    break
print(bags.get('shiny gold') - 1)
