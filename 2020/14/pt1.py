# Find this puzzle at:
# https://adventofcode.com/2020/day/14

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
memory = {}


def apply_mask(xy):
    """
    Apply bitmask to value.

    Args:
    xy: A tuple with the bit of the mask
    and the bit to mask (mask, value).

    Returns:
    The bit after being masked.
    """
    if xy[0] == 'X':
        return xy[1]
    else:
        return xy[0]


for line in puzzle_input:
    command, value = line.split(' = ')
    # Store the new mask
    if command == 'mask':
        mask = value
    # Mask the value and store its decimal value in memory
    else:
        address = int(''.join(i for i in command if i.isdigit()))
        value = bin(int(value))[2:].zfill(36)
        masked_value = ''.join(map(apply_mask, zip(mask, value)))
        memory[address] = int(masked_value, 2)
print(sum(memory.values()))
