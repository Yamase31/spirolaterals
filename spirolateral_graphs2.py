# Python program to demonstrate spirolateral graph drawing and relationships
# @author: James Lawson and William Xue

from turtle import Turtle, Screen
from random import seed
from random import randint

#seed is set
seed(1)

# turtle object is created
t = Turtle()
t.speed(0)
screen = Screen()

# Test sequences up to:
sequenceLength = 10

# Test from starting sequence
startingSeq = 1

# Generates data set for ordered sequences
myData = []
for i in range(startingSeq, sequenceLength + 1):

    #random movement value from 1 to 10
    value = randint(0,10)
    
    orderedSequence = [range(1, value)]

    # Initializes variables
    isClosed = False
    t.reset()
    initialPos = t.pos()

    # Draws Turtle
    for iterations in range(4):
        for turn in range(1, value):
            t.forward(turn * 10)
            t.left(90)
        if int(t.distance(initialPos)) == 0:
            isClosed = True

    data = {
        "Length": value,
        "Closed": str(isClosed),
        "Sequence": str(orderedSequence)
    }
    
    myData.append(data)
    screen.textinput("End of sequence", "Press OK to continue")

for i in range(sequenceLength - startingSeq + 1):
    print(myData[i]["Length"], "is closed:" + myData[i]["Closed"])


    
