# Python program to demonstrate spirolateral graph drawing and relationships
# @author: James Lawson

#turtle library is imported
import turtle 

#turtle object is created
t = turtle.Turtle()

#angle that the graphs turns
turningAngle = 90

#number of turns
numberOfTurns = 16

#number of repitions
repitions = 4

#total turning angle is calculated
totalTurningAngle = turningAngle * numberOfTurns * repitions

#for loop where the image is printed
for x in range(repitions):
    t.right(turningAngle)
    t.forward(90)
    t.right(turningAngle)
    t.forward(20)
    t.right(turningAngle)
    t.forward(10)
    t.right(turningAngle)
    t.forward(39)
    t.right(turningAngle)
    t.forward(50)
    t.right(turningAngle)
    t.forward(40)
    t.right(turningAngle)
    t.forward(60)
    t.right(turningAngle)
    t.forward(70)
    t.right(turningAngle)
    t.forward(80)
    t.right(turningAngle)
    t.forward(100)
    t.right(turningAngle)
    t.forward(110)
    t.right(turningAngle)
    t.forward(120)
    t.right(turningAngle)
    t.forward(130)
    t.right(turningAngle)
    t.forward(140)
    t.right(turningAngle)
    t.forward(150)
    t.right(turningAngle)
    t.forward(160)
    

#total turning angle is printed
print("Total Turning Angle: " + str(totalTurningAngle))

#modulo operation is calculated
modulo = totalTurningAngle%360

#total turning angle is printed
print(str(totalTurningAngle) + " % 360 = " + str(modulo))

#print statement
if (modulo == 0):
    print("It is a closed spirolateral graph!")
else:
    print("It is not a closed spirolateral graph!")
