# Find this puzzle at:
# https://adventofcode.com/2020/day/14
# Note! This code is largely inefficient!
# Purposefully avoided the use of any external libraries.
# It is just a one-time thing of me getting the answer.

import itertools
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
        return xy[0]
    elif xy[0] == '1':
        return xy[0]
    else:
        return xy[1]


def all_addresses(address):
    """
    Find all possible addresses of a masked address.

    Args:
    address: A masked address.

    Returns:
    All possible addresses of the masked address.
    """
    # How this function works is it find all the possible
    # combinations of X (e.g. 000, 001, 011, 111)
    # and then it finds all the unique permutations of each combination
    # (e.g. for 001: 001, 010, 100). Then each unique permutation is tested
    # with the original address and the decimal value stored.
    address = list(address)
    addresses = []
    pos_permutations = set()
    x_locations = [idx for idx, x in enumerate(address) if x == 'X']
    pos_combinations = [''.zfill(len(x_locations))]
    for idx in range(len(pos_combinations[0])):
        combination = list(pos_combinations[idx])
        combination[idx] = '1'
        pos_combinations.append(''.join(combination))
    for i in pos_combinations:
        pos_permutations |= {x for x in itertools.permutations(i, len(i))}
    for pos_permutation in pos_permutations:
        for bit in list(zip(pos_permutation, x_locations)):
            value, idx = bit
            address[idx] = value
        addresses.append(int(''.join(address), 2))
    return(addresses)


for line in puzzle_input:
    command, value = line.split(' = ')
    # Store the new mask
    if command == 'mask':
        mask = value
    # Find all addresses of the masked address
    # and write the value to those addresses
    else:
        dec_address = int(''.join(i for i in command if i.isdigit()))
        bi_address = bin(dec_address)[2:].zfill(36)
        masked_address = ''.join(map(apply_mask, zip(mask, bi_address)))
        for address in all_addresses(masked_address):
            memory[address] = int(value)
print(sum(memory.values()))
