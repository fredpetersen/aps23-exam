#! usr/bin/env python3
from sys import stdin, exit
import re

max_gins = 100
max_tonics = 100
max_people = 10e6
max_units_of_drinks = 10e6

max_allergenics = 100

g, i, n = next(stdin).split()
assert re.match(r"\d+", g)
assert re.match(r"\d+", i)
assert re.match(r"\d+", n)
g = int(g)
i = int(i)
n = int(n)
assert g <= max_gins
assert i <= max_tonics
assert n <= max_people

all_allergens = set()

for _ in range(g):
    line = next(stdin)
    assert re.match(r"^[1-9]\d*(( \w+)+| )$", line)
    units, *allergens = line.split()
    assert int(units) <= max_units_of_drinks
    for allergen in allergens:
        all_allergens.add(allergen)

for _ in range(i):
    line = next(stdin)
    assert re.match(r"^[1-9]\d*(( \w+)+| )$", line)
    units, *allergens = line.split()
    assert int(units) <= max_units_of_drinks
    for allergen in allergens:
        all_allergens.add(allergen)

for _ in range(n):
    line = next(stdin)
    assert re.match(r"^\w{1,10}(( \w+)+| )$", line)
    _, *allergens = line.split()
    for allergen in allergens:
        all_allergens.add(allergen)

assert len(all_allergens) <= max_allergenics

assert stdin.readline() == "" # no junk at the end

exit(42) # exit kattis-fully
