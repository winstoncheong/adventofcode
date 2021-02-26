import hashlib

f = open('day4in.txt')
start = f.readline()

val = 1

while True:
    test_str = start+str(val)
    result = hashlib.md5(test_str.encode())

    if result.hexdigest().startswith('00000'):
        print('Ans 1:', val)
        break

    val += 1

while True: 
    test_str = start+str(val)
    result = hashlib.md5(test_str.encode())

    if result.hexdigest().startswith('000000'):
        print('Ans 2:', val)
        break

    val += 1