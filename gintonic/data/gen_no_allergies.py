#!/usr/bin/python3

# Input generator, g, i and n before g gins with allergenics, i tonics with allergenics and g people with allergens.

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

random.seed(int(cmdlinearg('seed', sys.argv[-1])))
g = int(cmdlinearg('g'))
i = int(cmdlinearg('i'))
n = int(cmdlinearg('n'))

print(str(g) + " " + str(i) + " " + str(n))

for _ in range(g): # gin
    units = random.randint(1, 1e5)
    print(str(units) + " ")

for _ in range(i): # tonics
    units = random.randint(1, 1e5)
    print(str(units) + " ")
    
for z in range(n): # people
    print("c"+ str(z) + " ")
