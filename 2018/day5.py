
f = open('day5in.txt')
data = f.readline()

replacement = []

# generate substrings that replace
for c in range(ord('a'), ord('z') + 1):
    replacement.append(chr(c) + chr(c-32))
    replacement.append(chr(c-32) + chr(c))

def fully_react(polymer):
    old_length = len(polymer)
    changed = True

    while changed:
        changed = False

        
        for r in replacement:
            polymer = polymer.replace(r,'')

        if len(polymer) < old_length:
            changed = True
            old_length = len(polymer)

    # no more replacements possible
    return polymer


print('Answer 1:', len(fully_react(data)))


# Part 2

shortest = len(data)

for c in range(ord('a'), ord('z') + 1):
    # remove all instances of a letter, and fully react

    removed = data.replace(chr(c), '').replace(chr(c-32),'')
    reacted = len(fully_react(removed))

    if reacted < shortest:
        shortest = reacted

print('Answer 2:', shortest)
    


