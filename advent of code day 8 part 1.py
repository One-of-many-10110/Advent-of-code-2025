# Day 8

from math import sqrt

with open("example.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")

for l, line in enumerate(inputfile):
    inputfile[l] = [list(map(int, line.split(",")))]
inputlength = len(inputfile)

# List of lists made with all the xyz co-ordinates
# in lists for circuits
# difficult maths now
# So with this maths, you have to do pythagoras with three dimensions
# the distance of point a to point b is equal to the square root of (point Ax - point Bx)^2 +(point Ay - point By)^2 + (point Az - point Bz)^2 
# Do something to compare all of the co ordinates while keeping a record of the shortest distance each time
# After that add the contents of the smallest of the two circuits into the others circut list

# inputfile[circuit[co-ordinates]]

# lowest = (lowestdistance, ((pointA index),(pointB index)))
for i in range(10):
    lowest = (1000000,((0),(0)))
    inputcopy = inputfile.copy()
    for ca, circuitA in enumerate(inputfile):
        for pa, pointA in enumerate(circuitA): 
            for cb, circuitB in enumerate(inputfile):
                for pb, pointB in enumerate(circuitB):
                    if pointB not in circuitA:
                        # long maths time
                        distance = (pointA[0] - pointB[0])^2 + (pointA[1] - pointB[1])^2 + (pointA[2] - pointB[2])^2
                        try:
                            distance = sqrt(distance)
                        except:
                            distance = sqrt(distance * -1)
                        if distance < lowest[0]:
                            lowest = (distance, ((ca,pa),(cb,pb))) 
    circuitA, circuitB = inputcopy[lowest[1][0][0]], inputcopy[lowest[1][1][0]]
    pointA, pointB = inputcopy[lowest[1][0][1]], inputcopy[lowest[1][1][1]]
    if len(circuitA) > len(circuitB):
        inputfile[lowest[1][0][0]].extend(circuitB)
        inputfile.remove(circuitB)
    else:
        inputfile[lowest[1][1][0]].extend(circuitA)
        inputfile.remove(circuitA)

pass
    


