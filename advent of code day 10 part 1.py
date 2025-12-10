# Day 10

from itertools import permutations

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n") 

opposites = {
    "." : "#",
    "#" : "."
}

# so a precursive thingy that adds one to the permutations calculated each time
# stops if it finds a solution that makes all lights work
# it will test all the smallest numbers of combinations first
# yippee

def smallestnumberofpresses(but, combinations, goal):
    for p in permutations(but, combinations):
        templights = list("."*len(goal))
        for b in p:
            for n in b:
                templights[int(n)] = opposites[templights[int(n)]]
        if templights == goal:
            return combinations
    if combinations >= len(but):
        return False
    else:
        return smallestnumberofpresses(but, combinations + 1, goal)


lights = []
buttons = []

for line in inputfile:
    splitline = line.split()
    lights.append(list(splitline[0].replace("[","").replace("]","")))
    buttons.append(splitline[1:-1])

for l, line in enumerate(buttons):
    for i, linebutcooler in enumerate(line):
        line[i] = linebutcooler.replace("(","").replace(")","").split(",")
    buttons[l] = line
    
count = 0

for i in range(len(lights)):
    count += smallestnumberofpresses(buttons[i], 1, lights[i])

print(str(count))

#for b, button in enumerate(buttons):
 #   currentlights = lights[b]
 #   templights = currentlights.copy()
 #   for i in permutations(button, len(currentlights)):
        
