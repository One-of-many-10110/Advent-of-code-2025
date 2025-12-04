# advent of code day 4

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")
inputlength = len(inputfile)
linelength = len(inputfile[0])

# for memory purposes, x is how far along one line, y is the line, from the top down.
def checkneighbors(x,y):
    # So this has got to check all the neighbors of the x and y in that array
    # maybe have a list of positions to check that can be modified for edges and such
    # so like if its on a top edge or a side edge remove positions that dont need to be checked
    # check that a corner position is not already removed before trying to remove for error reasons
    # if the count ever goes above 4, no more checks are required so you can just return false there
    # you can check the number of checks left and end if the number of check wont change anything even if they are all rolls return true
    global inputfile , inputlength , linelength
    rollcount = 0
    checkingpositions = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]# added on to the x and y in that order to get adjacent things
    removedpositions = []
    if y == 0:
        for i in range(-1,2): 
            if (i,-1) not in removedpositions: 
                removedpositions.append((i,-1))
    elif y == inputlength - 1:
        for i in range(-1,2): 
            if (i,1) not in removedpositions: 
                removedpositions.append((i,1))
    if x == 0:
        for i in range(-1,2): 
            if (-1,i) not in removedpositions: 
                removedpositions.append((-1,i))
    elif x == linelength - 1:
        for i in range(-1,2): 
            if (1,i) not in removedpositions: 
                removedpositions.append((1,i))
    for removed in removedpositions:
        checkingpositions.remove(removed)
    for a in range(len(checkingpositions)):
        addition = checkingpositions[a]
        if inputfile[y+addition[1]][x+addition[0]] == "@":
            rollcount += 1
            if rollcount >= 4:
                return False
        else:
            if rollcount + (len(checkingpositions )- 1) - a < 4:
                return True
            
moveablecount = 0

for r in range(inputlength):
    for c in range(linelength):
        if inputfile[r][c] == "@":
            # just add one if it returned true
            # all the hard stuff done by the function really
            canmove = checkneighbors(c,r)
            if canmove == True:
                moveablecount += 1
                print("Added 1")

print(f"The final result was {moveablecount}.")