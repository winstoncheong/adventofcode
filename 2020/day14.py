from collections import defaultdict
import re

#f = open('testin.txt')
f = open('day14in.txt')
lines = [line.strip() for line in f.readlines()]

mask = ''
memory = defaultdict(int)

def int_to_bitstring(v):
    """Convert int into bitstring"""
    repr = bin(int(v))[2:]
    bitstring = repr.rjust(36, '0')
    return bitstring

def apply_mask(mask, val):
    """Apply mask to value. Return resulting value."""
    res = []
    for m, v in zip(mask, val):
        if m == 'X':
            res.append(v)
        else:
            res.append(m)
    return ''.join(res)


def get_addresses(mask_str):
    """Use a masked string to specify addresses. Return all addresses that match"""

    res = [] # contains all output matching the mask string

    if 'X' not in mask_str:
        return [mask_str]

    i = mask_str.find('X')
    pre = mask_str[0:i] # capture everying before first branching point

    recurse = get_addresses(mask_str[i+1:])
    
    for val in recurse:
        res.append(pre+'0'+val)
        res.append(pre+'1'+val)

    return res

def apply_mask2(mask, addr):
    """For part 2. Apply mask to address, return list of addresses"""
    masked = []
    for m, a in zip(mask, addr):
        if m == '0':
            masked.append(a)
        else: #either = '1' or 'X', will use that character
            masked.append(m)

    return get_addresses(''.join(masked))

# Part 1
for line in lines:
    parts = line.split(' ')
    #print(parts)

    if parts[0] == 'mask':
        # ['mask', '=', 'X10X11X1000101X1XX001100001X101X0111']
        mask = parts[-1]

    else:
        # ['mem[27041]', '=', '56559']
        val = int_to_bitstring(parts[-1])
        
        m = re.match(r'mem\[(\d*)\]', parts[0])
        addr = m.group(1)
        #print(addr, val)
        
        memory[addr] = apply_mask(mask, val)

# Convert back
ans1 = sum(int(v, base=2) for v in memory.values())
print("Ans 1:", ans1)


# Part 2
# Bitmask applies to memory addresses instead of values.
# I'll store values as they are, without converting.
# Keys may as well stay in binary representation
memory=defaultdict(int)

for line in lines:
    parts = line.split(' ')

    if parts[0] == 'mask':
        # ['mask', '=', 'X10X11X1000101X1XX001100001X101X0111']
        mask = parts[-1]

    else:
        # ['mem[27041]', '=', '56559']
        val = int(parts[-1])
        
        m = re.match(r'mem\[(\d*)\]', parts[0])
        addr = m.group(1)

        addresses = apply_mask2(mask, int_to_bitstring(addr))

        for address in addresses:
            memory[address] = val

ans2 = sum(memory.values())
print('Ans 2:', ans2)