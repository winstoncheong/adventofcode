f = open('day1in.txt','r')
lines = f.readlines()
vals = [ int(line.strip()) for line in lines]
vals.sort()
print(vals)

for i in vals:
	for j in vals:
		if i + j == 2020:
			print("Part 1: ", i*j)
			break
	else:
		continue
	break


for i in vals:
	for j in vals:
		for k in vals:
			if i + j + k == 2020:
				print("Part 2: ", i*j*k)
				break
		else: 
			continue
		break
	else:
		continue
	break


