# Find this puzzle at:
# https://adventofcode.com/2020/day/13

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
arrival = int(puzzle_input[0])
buses = puzzle_input[1].split(',')
close_bus_time = float("inf")
for bus in buses:
    if bus != 'x':
        bus = int(bus)
        # If the bus comes right when you arrive,
        # the answer is 0, because you have to wait 0 minutes.
        if arrival % bus == 0:
            print(0)
            break
        # Else calculate the closest departure time after you arrive
        else:
            bus_time = bus * (arrival//bus + 1)
        # Store the ID and the time of departure of the closet bus
        if min(close_bus_time, bus_time) == bus_time:
            close_bus_id = bus
            close_bus_time = bus_time
print((close_bus_time - arrival) * close_bus_id)
