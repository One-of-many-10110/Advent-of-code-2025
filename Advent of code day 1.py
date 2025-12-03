# My silly advent of code code thing

zerocount = 0
newposition = 50

with open("Documents/Silly programs/Python/required files/input day 1.txt",mode="r",encoding="utf-8-sig") as file:
    instructionlist = file.read().split()

print(f"starting at {newposition}")

for instruction in instructionlist:
    zerobuffer = 0
    currentposition = newposition
    difference = 0
    number = int(instruction[1:len(instruction)])
    if instruction[0] == "L":
        number *= -1
    newposition += number
    while newposition > 99:
        newposition -= 100
        if newposition != 0:
            zerocount += 1
    if newposition < 0:
        while newposition < 0:
            zerobuffer += 1
            newposition += 100
        if currentposition == 0:
            zerobuffer -= 1
        zerocount += zerobuffer
    if newposition == 0:
        zerocount += 1
    print(f"Rotated {instruction} and ended at point {newposition}. Current zerocount is {zerocount}")
print(f"There were {zerocount} zeros in that thing.")
    
        
    