f = open('day2in.txt')
lines = f.readlines()

ans1 = 0
ans2 = 0

for line in lines:
    l,w,h = map(int, line.split('x'))

    ans1 += 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)
    ans2 += l*w*h + min(2*(l+w), 2*(w+h), 2*(h+l))

print('Ans 1: ', ans1)
print('Ans 2: ', ans2)
