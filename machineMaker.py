#makes machines
import random
import os.path

#maybe have it check for machines already in the folder?
fileName = "machine.py"


if(os.path.exists(fileName)):
	machineFile = open(fileName, "w")
else:
	machineFile = open(fileName, "x")
	machineFile = open(fileName, "w")


machineFile.write("from turtle import *\n")
machineFile.write("import random\n\n")

msg = "def makeColor():\n"
msg += "\tr = lambda: random.randint(0,255)\n"
msg += "\treturn('#%02X%02X%02X' % (r(),r(),r()))\n"

machineFile.write(msg)


msg = "clr = makeColor()\n"
msg += "color(clr)\n"
machineFile.write(msg)

canvasText = "penup()\nbegin_fill()\ngoto(-300, 300)\nforward(600)\nseth(270)\nforward(600)\nseth(180)\nforward(600)\nseth(90)\nforward(600)\nend_fill()\n"
machineFile.write(canvasText)

numShapes = random.randint(1, 10)
machineFile.write("for i in range(0, " + str(numShapes) + "):\n")

#this part makes the shapes
#random color for the shape
msg = "\tclr = makeColor()\n"
msg += "\tcolor(clr)\n"
machineFile.write(msg)

#go to the first point of the shape
machineFile.write("\tpenup()\n")
msg = "\tx = random.randint(-300, 300)\n"
msg += "\ty = random.randint(-300, 300)\n"
msg += "\tgoto(x, y)\n"
msg += "\tpendown()\n"
machineFile.write(msg)

#number of sides for the shape
msg = "\tnumSides = random.randint(2, 7);\n"
msg += "\tbegin_fill()\n"
msg += "\tfor i in range(0, numSides):\n"
machineFile.write(msg)

#drawing the sides
msg = "\t\tlen = random.randint(10, 100)\n"
msg += "\t\tangle = random.randint(0, 180)\n"
choice = random.randint(0, 1)
if(choice == 0):
	direction = "left"
else:
	direction = "right"
msg += "\t\t" + direction + "(angle)\n"
msg += "\t\tforward(len)\n"
machineFile.write(msg)

msg = "\tend_fill()\n"
machineFile.write(msg)

msg = "hideturtle()\ndone()\n"
machineFile.write(msg)

machineFile.close()