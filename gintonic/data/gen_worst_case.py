#!/usr/bin/python3

# Input generator, g, i and n before g gins with allergenics, i tonics with allergenics and g people with allergens.

import string
import sys
import random

from itertools import combinations

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    if default is None:
        print("missing parameter", name)
        sys.exit(1)
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))

allergies=10
allergens = []

for c in string.ascii_lowercase[:4]:
    for k in string.ascii_lowercase:
        allergens.append(c + k)

allergens = allergens[:allergies]
allergy_combinations = []
for i in range(1,11):
  allergy_combinations.extend(combinations(allergens,i))

g = 100
i = 100
n = 10000

x = 0

print(str(g) + " " + str(i) + " " + str(n))

for _ in range(g): # gin
    units = random.randint(1, 10)
    print(str(units) + " " + " ".join(allergy_combinations[x % len(allergy_combinations)]))
    x+=1

for _ in range(i): # tonics
    units = random.randint(1, 10)
    print(str(units) + " " + " ".join(allergy_combinations[x % len(allergy_combinations)]))
    x+=1
    
for z in range(n): # people
    print("c"+ str(z) + " " + " ".join(allergy_combinations[x % len(allergy_combinations)]))
    x+=1
