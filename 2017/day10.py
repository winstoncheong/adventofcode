from itertools import cycle, islice, chain
import functools

f = open('day10input.txt')
length_seq = list(map(int, f.readline().strip().split(',')))
LISTLEN = 256


# Example
# length_seq = list(map(int, "3,4,1,5".split(',')))
# LISTLEN = 5

class CyclicList:

    def __init__(self, iterable, offset=0):
        self._list = list(iterable)
        self.offset = offset

    def __len__(self):
        return len(self._list)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self[ii] for ii in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            index = (key + self.offset) % len(self)
            return self._list[index]
        else:
            raise TypeError(f'Invalid argument {key}')

    def __str__(self):
        return str(self[0:len(self)])

    def shift(self, n):
        self.offset += n
        self.offset %= len(self)


def knot_hash_round(length_seq, num_rounds):
    """
    Executes num_rounds of the Knot Hash, using the length_seq for each round.
    :param length_seq:
    :param num_rounds:
    :return:
    """
    skip = 0
    total_shifted = 0
    c = CyclicList(range(LISTLEN))

    for round in range(num_rounds):
        # print(f'Round {round}:')

        for length in length_seq:
            selected = c[:length]
            # print(f'Selected: {selected}')

            c = CyclicList(list(reversed(c[:length])) + c[length:len(c)])
            assert len(c) == LISTLEN
            # print(f'After reversing {length}')
            # print(c)

            # move current position
            c.shift(length + skip)
            total_shifted += length + skip

            # print(f'After shifting {length + skip}')
            # print(c)

            skip += 1
            # print(f'Skip is now {skip}')

    # shift back to index correctly
    c.shift(-total_shifted)
    # print(f'Undoing all shifting: {c}')

    return c


def condense_hash(lst):
    res = []
    # print(lst)
    for i in range(256 // 16):
        block = lst[16 * i: 16 * (i + 1)]
        # print(block)
        res.append(functools.reduce(lambda x, y: x ^ y, block))

    # convert to hex string
    hexstring = ''.join([hex(i)[2:].zfill(2) for i in res])

    return hexstring


def str2length_seq(str):
    length_seq = list(map(ord, str))
    length_seq.extend([17, 31, 73, 47, 23])
    return length_seq


def knot_hash(string):
    # For part 2

    length_seq = str2length_seq(string)
    c = knot_hash_round(length_seq, 64)  # circular list with sparse hash

    hexstring = condense_hash(c)
    return hexstring


# Check examples
# print(knot_hash(""))
# print(knot_hash("AoC 2017"))
# print(knot_hash("1,2,3"))
# print(knot_hash("1,2,4"))

c = knot_hash_round(length_seq, 1)
print(f'Ans 1: {c[0] * c[1]}')

# Part 2
f = open('day10input.txt')
line = f.readline().strip()
print(f'Ans 2: {knot_hash(line)}')
