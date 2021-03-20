import string
f = open('day11in.txt')
pw = f.readline()

disallowed = 'iol'
alphabet = string.ascii_lowercase

def contains_triple_straight(pw):
    for i in range(len(alphabet) - 2):
        # print(alphabet[i:i+3])
        if alphabet[i:i+3] in pw:
            return True
    return False

def has_two_pairs(pw):
    pairs = 0
    i = 0
    while i < len(pw):
        if len(pw) > i + 1 and pw[i]==pw[i+1]:
            pairs += 1
            i += 2
        else:  
            i += 1
    return pairs >= 2

def incr_pass(pw):
    ords = list(map(ord, list(pw)))

    i = -1
    ords[i] += 1 
    while ords[i] == ord('z') + 1: 
        ords[i] = ord('a') # loop around 
        # carry over
        i -= 1
        ords[i] += 1

    return ''.join(map(chr, ords))

def does_not_contain_disallowed(pw):
    for c in disallowed:
        if c in pw:
            return False
    return True

def is_valid_pass(pw):
    return contains_triple_straight(pw) and has_two_pairs(pw) and does_not_contain_disallowed(pw)



while not is_valid_pass(pw):
    pw = incr_pass(pw)

print('Answer 1:', pw)

pw = incr_pass(pw)
while not is_valid_pass(pw):
    pw = incr_pass(pw)

print('Answer 2:', pw)
