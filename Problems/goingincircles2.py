# https://open.kattis.com/problems/goingincircles

import random
import json
import time

def read_state():
    with open('state.txt', 'r') as f:
        return json.load(f)

def write_state(state):
    with open('state.txt', 'w') as f:
        json.dump(state, f)

def initialize():
    state = {}
    state["randlength"] = 50

    # Build a random sequence of {0,1} not seeded with E, PI etc. of length ~50. Make sure it starts with a 1
    state["randpattern"] = [1]
    for i in range(state["randlength"] - 1):
        state["randpattern"].append(random.randint(0, 1))

    state["iterations"] = 0
    state["i"] = 0

    # Variable that holds last steps
    state["carriages"] = []
    state["justflip"] = False
    write_state(state)

def ans(currentCarriage):
    state = read_state()

    # Build the first `randlength` steps to the right to be all 0s
    if state["iterations"] < state["randlength"]:
        if currentCarriage == 1:
            return "? flip"
        state["iterations"] += 1
        write_state(state)
        return "? right"

    # Start building the random sequence from place 50 and going left
    if state["iterations"] < 2* state["randlength"]:
        if currentCarriage == 1 and state["i"] != 0 and not state["justflip"]:
            # If during building you hit the 1 that you started by building, you know the length is less than 50
            return "! " + str(state["i"])
        if currentCarriage != state["randpattern"][state["i"]]:
            #print("I flip because:")
            #print("currentCarriage", currentCarriage)
            #print("state[randpattern][state[i]]", state["randpattern"][state["i"]])
            #print("state[i]", state["i"])
            #time.sleep(3)
            #state["i"] += 1
            state["justflip"] = True
            write_state(state)
            return "? flip"
        state["i"] += 1
        state["iterations"] += 1
        state["justflip"] = False
        write_state(state)
        return "? left"
    
    if (not checkmatch(state)):
        state["carriages"].append(currentCarriage)
        write_state(state)
        return "? left"
    temp = (len(state["carriages"]))
    return ( "! " + str(temp))

# function to check if last 50 steps match my random pattern

def checkmatch(state):
    if len(state["carriages"]) < state["randlength"]:
        return False
    for i in range(state["randlength"]):
        if state["carriages"][len(state["carriages"]) - i - 1] != state["randpattern"][state["randlength"] - i - 1]:
            return False
    

    return True

# otherwise after building the 50 steps continue going left looking for the pattern


# once pattern is hit calculate how many steps have been walked until hitting this
