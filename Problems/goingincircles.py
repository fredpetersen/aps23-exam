# https://open.kattis.com/problems/goingincircles

import random

randlength = 5

# Build a random sequence of {0,1} not seeded with E, PI etc. of length ~50. Make sure it starts with a 1
randpattern = [1]
for i in range(randlength - 1):
    randpattern.append(random.randint(0, 1))

print(randpattern)

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
    if currentCarriage == 1 & i != 0:
        print("!", i)
        quit() # This seems to work and print the correct length!
    if currentCarriage != randpattern[i]:
        print("? flip")
        currentCarriage = int(input())
    print("? left")
    currentCarriage = int(input())
    
# otherwise after building the 50 steps continue going left looking for the pattern

currentMatchLength = 0
numsteps = 0
while (currentMatchLength < len(randpattern)):
    if currentCarriage == randpattern[currentMatchLength]:
        currentMatchLength += 1
    else:
        currentMatchLength = 0
    
    print("? left")
    currentCarriage = int(input())
    numsteps += 1

# once pattern is hit calculate how many steps have been walked until hitting this
print("!", numsteps)


# start (len: 7)
# 0100011 

# state
# 0110011
# x
# pos