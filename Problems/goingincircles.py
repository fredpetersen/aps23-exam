# https://open.kattis.com/problems/goingincircles

import random

randlength = 50

# Build a random sequence of {0,1} not seeded with E, PI etc. of length ~50. Make sure it starts with a 1
# Starts with 1 because this is used to check that n !< randlength 
# (if building randlength hits 1 then n = how much of randpattern has been built)
randpattern = [1]
for i in range(randlength - 1):
    randpattern.append(random.randint(0, 1))

currentCarriage = int(input())

# Build the first `randlength` steps to the right to be all 0s
for _ in range(randlength):
    if currentCarriage == 1:
        print("? flip")
        currentCarriage = int(input()) # this should always be 0
    print("? right")
    currentCarriage = int(input())

# Start building the random sequence from place 50 and going left
for i in range(randlength):
    # If during building you hit the 1 that you started by building, you know the length is less than 50
    if currentCarriage == 1 and i != 0:
        print("!", i)
        quit() # This seems to work and print the correct length!
    if currentCarriage != randpattern[i]:
        print("? flip")
        currentCarriage = int(input())
    print("? left")
    currentCarriage = int(input())

# Variable that holds last steps

carriages = []

# function to check if last 50 steps match my random pattern

def checkmatch():
    if len(carriages) < randlength:
        return False
    for i in range(randlength):
        if carriages[len(carriages) - i - 1] != randpattern[randlength - i - 1]:
            return False
    return True

# otherwise after building the 50 steps continue going left looking for the pattern

while (not checkmatch()):
    print("? left")
    carriages.append(int(input()))

# once pattern is hit calculate how many steps have been walked until hitting this
print("!", len(carriages) + 1) # without +1 it fails at TC2
