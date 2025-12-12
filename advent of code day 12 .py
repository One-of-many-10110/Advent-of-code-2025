# Day 12

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().strip().split("\n") 

minvalues = {}
hashcount = 0

for line in inputfile:
    if len(line) < 4:
        if line == "":
            minvalues.update({currentnum : hashcount})
            hashcount = 0
        elif line[0].isnumeric():
            currentnum = int(line[0])
        else:
            for char in line:
                if char == "#":
                    hashcount += 1
    else:
        startindex = inputfile.index(line)
        break

trees = inputfile[startindex:]

for t in range(len(trees)):
    tree = trees[t].split(":")
    tree[0] = list(map(int, tree[0].split("x")))
    tree[1] = list(map(int, tree[1].strip().split(" ")))
    trees[t] = tree

# minimum part:
minimumfilled = 0
for tree in trees:
    currentarea = tree[0][0] * tree[0][1]
    requirementarea = 0
    for requirement in tree[1]:
        requirementarea += requirement * 9
    if requirementarea <= currentarea:
        minimumfilled += 1

# maximum part:
maximumfilled = 0
for tree in trees:
    currentarea = tree[0][0] * tree[0][1]
    requirementarea = 0
    for r, requirement in enumerate(tree[1]):
        requirementarea += requirement * minvalues[r]
    if requirementarea <= currentarea:
        maximumfilled += 1

print(f"The minumum number of trees that you can fill is {minimumfilled} and the maximum is {maximumfilled}")