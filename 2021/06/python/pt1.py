import os
with open(f'{os.path.dirname(__file__)}/../input.txt', 'r') as file:
    fishes = [int(i) for i in file.read().split(',')]


def growth(born_day):
    """
    Calculate the growth of the fish population given one fish.

    Args:
        born_day (int): The day the initial fish was born.

    Returns:
        int: The number of fish that is a descendant of the initial fish.
    """
    count = 1
    born_day -= 2
    while True:
        born_day -= 7
        if born_day <= 0:
            return count
        else:
            count += growth(born_day)


count = 0
# No need to count fishes born on the same day
# they will have the same amount of descendants
for i in set(fishes):
    # Multiply by total number of fishes born on the same day
    count += fishes.count(i) * growth(80 + (7 - i) + 2)

print(count)
