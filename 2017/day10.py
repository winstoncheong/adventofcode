from itertools import cycle, islice, chain

# TODO: There is some mistake?

f = open('day10input.txt')
line = list(map(int, f.readline().strip().split(',')))
LISTLEN = 256

# Example 
##line = list(map(int, "3,4,1,5".split(',')))
##LISTLEN = 5

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
        
c = CyclicList(range(LISTLEN))
# current position handled by CyclicList
skip = 0
print(c)

for length in line:
    
    c = CyclicList(list(reversed(c[:length])) + c[length:len(c)])
    assert len(c)==LISTLEN
    print(f'After reversing {length}')
    print(c)
    
    # move current position
    c.shift(length+skip)

    print(f'After shifting {length+skip}')
    print(c)

    skip += 1

    

print(f'ans: {c[1]*c[2]}')
