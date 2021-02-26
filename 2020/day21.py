import re
import itertools 

from collections import defaultdict
from pprint import pprint 

# f = open('testin.txt')
f = open('day21in.txt')
lines = [line.strip() for line in f.readlines()]

# each food is a dict {'ingredients': [word, word, ...], 'allergens', [allergen, allergen, ...]}
foods = []

# restructure data into foods variable
for line in lines:
    a = re.match(r'.*\(contains (.*)\)', line)
    i = re.match(r'^(.*) \(contains.*\)', line)

    foods.append(dict(ingredients=i.group(1).split(' '), allergens=a.group(1).split(', ')))

# pprint(foods)

# create set of all allergens
allergens = set().union(*(food['allergens'] for food in foods))
# print(allergens)

# dictionary that maps allergen -> list(ingredients)
potentially_contains = {}

# for each allergen, intersect all word-lists. 
for allergen in allergens:
    # get all wordlists where the allergen is found
    wordlists = [ food['ingredients'] for food in foods if allergen in food['allergens'] ]

    # intersect them
    potential_words = set.intersection(*map(set, wordlists))
    # pprint(wordlists)
    # print('potential words: ', potential_words)

    potentially_contains[allergen] = potential_words

print(potentially_contains)

# if the list of ingredients potentially containing an allergen is exactly size 1, 
# that ingredient must contain the allergen, and any other occurrences of that ingredient can be removed from "potentially_contains"
# since "Each allergen is founded in exaclty one ingredient."

# dict mapping ingredient -> allergen
contains_allergen = {}

# list of tuples (allergen, ingredient) 
# that can be removed from potentially_contains
to_simplify = ['a']

while to_simplify:
    to_simplify = []

    # populate contains_allergen
    for allergen, ingredients in potentially_contains.items():
        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            contains_allergen[ingredient] = allergen
            to_simplify.append((allergen, ingredient))

    # simplify contains_allergen
    for allergen, ingredient in to_simplify:
        del potentially_contains[allergen]
        for a, i_list in potentially_contains.items():
            if ingredient in i_list:
                i_list.remove(ingredient)

    # print(potentially_contains)

print('Potential:', potentially_contains)
print('Certain:', contains_allergen)

# Assumption that potentially_contains is empty, that all mappings from allergen to ingredient are found
unsafe_ingredients = list(contains_allergen.keys())

print('Unsafe:', unsafe_ingredients)

# Produce part 1 answer

occurrences = list(filter(lambda x: x not in unsafe_ingredients, itertools.chain.from_iterable([food['ingredients'] for food in foods])))
# print(occurrences)
print('Ans 1:', len(occurrences))

# Part 2 

# Sort the contains_allergen dictionary by values
# Ingredients will be in allergen-alphabetical order  
sorted_ingredients = sorted(contains_allergen, key=contains_allergen.get)
print(sorted_ingredients)

print('Ans 2: ', ','.join(sorted_ingredients))