import os
with open(f'{os.path.dirname(__file__)}/../input.txt', 'r') as file:
    commands = file.read().splitlines()

hor = depth = aim = 0
for i in commands:
    command, num = i.split()
    num = int(num)
    if command == "up":
        aim -= num
    elif command == "down":
        aim += num
    elif command == "forward":
        hor += num
        depth += aim * num

print(hor * depth)
