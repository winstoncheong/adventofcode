import re
f = open('day15in.txt')
reg = r'(\w*): capacity (-?\d*), durability (-?\d*), flavor (-?\d*), texture (-?\d*), calories (-?\d*)'
CALORIE_TARGET = 500

lines = f.readlines()

ingredients = []

for line in lines:
    m = re.match(reg, line)
    ingredients.append(tuple(map(int,m.groups()[1:])))

# print(ingredients)
assert len(ingredients) == 4
# This code assumes there are only 4 ingredients by using a triply-nested for loop.

def dot_product(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))


max_score = -1
max_score2 = -1

for x in range(0, 100):
    for y in range(0, 100 - x):
        for z in range(0, 100 - x - y):
            # print((x, y, z, 100-x-y-z))
            w = 100 - x - y - z # last ingredient

            v_amt = [x,y,z,w]
            v0 = [ing[0] for ing in ingredients]
            v1 = [ing[1] for ing in ingredients]
            v2 = [ing[2] for ing in ingredients]
            v3 = [ing[3] for ing in ingredients]
            v4 = [ing[4] for ing in ingredients]

            capacity = dot_product(v_amt, v0)
            durability = dot_product(v_amt, v1)
            flavor = dot_product(v_amt, v2)
            texture = dot_product(v_amt, v3)
            calories = dot_product(v_amt, v4)


            if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
                score = 0
            else:
                score = capacity * durability * flavor * texture

            if score > max_score:
                # print(capacity, durability, flavor, texture, 'using', v_amt, v0, v1, v2, v3)
                max_score = score
            
            if score > max_score2 and calories == CALORIE_TARGET:
                max_score2 = score

print('Ans 1:', max_score)
print('Ans 2:', max_score2)