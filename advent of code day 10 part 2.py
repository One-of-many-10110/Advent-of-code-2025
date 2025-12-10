# Day 10

from itertools import product

with open("example.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n") 

opposites = {
    "." : "#",
    "#" : "."
}

# recursion actually sets me up well for this
# I have a statement already that will return the combinations if templights == goal
# all i got to do now is do the simutaneous equasion stuff exclusively for the combinations that pass the first test and result in the coal light combo
# oh wait but you also cant use the permutations thing
# oh no
# i could use product instead
# that would include duplicates...
# that feels like it shouldnt work

def smallestnumberofpresses(but, combinations, goal, goaltage):
    for p in product(but, repeat = combinations):
        templights = list("."*len(goal))
        for b in p:
            for n in b:
                templights[int(n)] = opposites[templights[int(n)]]
        if templights == goal:
            print(str(combinations))
            return combinations
    return smallestnumberofpresses(but, combinations + 1, goal)


lights = []
buttons = []
joltage = []

for line in inputfile:
    splitline = line.split()
    lights.append(list(splitline[0].replace("[","").replace("]","")))
    buttons.append(splitline[1:-1])
    joltage.append(splitline[-1].replace("{","").replace("}",""))


for l, line in enumerate(buttons):
    for i, linebutcooler in enumerate(line):
        line[i] = linebutcooler.replace("(","").replace(")","").split(",")
    buttons[l] = line
    
count = 0

for i in range(len(lights)):
    count += smallestnumberofpresses(buttons[i], 1, lights[i], joltage[i])

print(str(count))

#for b, button in enumerate(buttons):
 #   currentlights = lights[b]
 #   templights = currentlights.copy()
 #   for i in permutations(button, len(currentlights)):
        
