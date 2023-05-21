#!/usr/bin/python3

# Input generator, g, i and n before g gins with allergenics, i tonics with allergenics and g people with allergens.
# This generator asserts low count of allergies for people to increase size of graph for hashing-like solutions

import string
import sys
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    if default is None:
        print("missing parameter", name)
        sys.exit(1)
    return default

allergens = []

allergies=int(cmdlinearg('allergies', 100))
max_units=int(cmdlinearg('max', 10e6))

for c in string.ascii_lowercase[:4]:
    for k in string.ascii_lowercase:
        allergens.append(c + k)

allergens = allergens[:allergies]

random.seed(int(cmdlinearg('seed', sys.argv[-1])))
g = int(cmdlinearg('g'))
i = int(cmdlinearg('i'))
n = int(cmdlinearg('n'))

print(str(g) + " " + str(i) + " " + str(n))

for _ in range(g): # gin
    units = random.randint(1, max_units)
    allergenics = random.randint(0, allergies)
    random.shuffle(allergens)
    print(str(units) + " " +" ".join(allergens[:allergenics]))

for _ in range(i): # tonics
    units = random.randint(1, max_units)
    allergenics = random.randint(0, allergies)
    random.shuffle(allergens)
    print(str(units) + " " +" ".join(allergens[:allergenics]))
    
for z in range(n): # people
    allergenics = random.randint(0, (allergies/10))
    random.shuffle(allergens)
    print("c"+ str(z) + " " +" ".join(allergens[:allergenics]))
