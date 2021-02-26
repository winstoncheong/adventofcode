

def fuel(mass):
    return max(0, mass//3 - 2)

def fuel_recurse(mass):
    curr_fuel = fuel(mass)
    new_fuel = curr_fuel
    while new_fuel > 0:
        new_fuel = fuel(new_fuel)
        # print(new_fuel)
        curr_fuel += new_fuel

    return curr_fuel


f = open('day1in.txt','r')
lines = f.readlines()

total1 = 0
total2 = 0

for line in lines:
    total1 += fuel(int(line))
    total2 += fuel_recurse(int(line))

print(f'Answer 1: {total1}')
print(f'Answer 2: {total2}')

# Test values
# print(fuel(1969))
# print(fuel_recurse(1969))