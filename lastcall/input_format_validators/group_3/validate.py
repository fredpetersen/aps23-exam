#! usr/bin/env python3
import sys
import re

# Adhere to scoring groups in README.md
# This is scoring group 3: ingredients = 10, wishes per person = 1

maxIngredients = 1000
maxUnitsPerIngredient = 1000

maxDrinks = 1000
maxIngredientsPerDrink = 10

maxPeople = 1000
maxWishesPerPerson = 1

line = sys.stdin.readline()
assert re.match(r"\d+", line)
ingredients = int(line)

valid_ingredients = []
valid_drinks = []

assert 1 <= ingredients <= maxIngredients

for i in range(ingredients):
    ingredient_line = sys.stdin.readline()
    regex = r"\w{1,10} \d+\n" # each line contains a name and a limit as a digit with no whitespace between the digit and the newline
    assert re.match(regex, ingredient_line), ingredient_line
    name, limit = ingredient_line.split()
    assert 1 <= limit < maxUnitsPerIngredient
    valid_ingredients.append(name)


line = sys.stdin.readline()
assert re.match(r"\d+", line)
drinks = int(line)

assert 1 <= drinks <= maxDrinks

for i in range(drinks):
    drinks_line = sys.stdin.readline()
    regex = r"(\w+ ){1,}(\w+)\n" # each line consists of a name + at least one ingredient and ending in a newline character without whitespace between the last ingredient and the newline
    assert re.match(regex, drinks_line), drinks_line
    name, ingredients = drinks_line.split(' ', 1)
    # assert that the list deos not contain duplicates?
    ingredients = ingredients.split()
    assert 1 <= len(ingredients) <= maxIngredientsPerDrink
    for j in range(ingredients):
        assert ingredients[j] in valid_ingredients
    valid_drinks.append(name)



line = sys.stdin.readline()
assert re.match(r"\d+", line)
people = int(line)

assert 1 <= people <= maxPeople

for i in range(people):
    person_line = sys.stdin.readline()
    regex = r"(\w+ ){1,}(\w+)\n" # each line consists of a name + at least one ingredient and ending in a newline character without whitespace between the last ingredient and the newline
    assert re.match(regex, person_line), person_line
    name, wishes = person_line.split(' ', 1)
    # assert that the list deos not contain duplicates?
    wishes = wishes.split()
    assert 1 <= len(wishes) <= maxWishesPerPerson
    for j in range(wishes):
        assert wishes[j] in valid_drinks
        

assert sys.stdin.readline() == "" # no junk at the end

sys.exit(42) # exit kattis-fully