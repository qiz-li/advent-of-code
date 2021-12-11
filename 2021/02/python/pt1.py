import os
with open(f'{os.path.dirname(__file__)}/../input.txt', 'r') as file:
    commands = file.read().splitlines()

hor = depth = 0
for i in commands:
    command, num = i.split()
    num = int(num)
    if command == "forward":
        hor += num
    elif command == "up":
        depth -= num
    elif command == "down":
        depth += num

print(hor * depth)
