
with open('day1input.txt') as f:
    line = f.readline().strip()
    

count = 0
for i in range(len(line)):
    if line[i] == line[i-1]: # this will handle the wrap around 
        count += int(line[i])

print(f"First answer: {count}")

# second part

halfway = len(line) // 2

count = 0
for i in range(len(line)):
    if line[i] == line[i-halfway]: # this will handle the wrap around 
        count += int(line[i])

print(f"Second answer: {count}")
