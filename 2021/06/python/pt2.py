import os
with open(f'{os.path.dirname(__file__)}/../input.txt', 'r') as file:
    raw = [int(fish) for fish in file.read().split(',')]
    fishes = [raw.count(timer) for timer in range(9)]

# Instead of tracking each individual fish
# we can just track the number of fish at each "timer"
for day in range(256):
    new_fish = fishes.pop(0)
    fishes[6] += new_fish
    fishes.append(new_fish)

print(sum(fishes))
