# Day 5

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")
    
emptyindex = inputfile.index("") # grab the index of the separator of the ranges and foods
ranges, foods = inputfile[:emptyindex], list(map(int, inputfile[emptyindex + 1:])) # split the list, not including the separator

# So, you convert the ranges into lists from the n-n state using .split("-")
# (while doing that record the highest and lowest values and add 1 to the second value so it works in range() easier)
# im sure there's something fancy you can do with conglomerating overlap into one range.
# i could be focusing on something that doesnt matter but it would be fun to code so screw it
# figure out how to conglomerate range overlap
# oh god i had an idea. sets. no duplicates means you can have a list of positions to check with no duplicate positions
# its (maybe) perfect
# oh i really wanna do that now
# oH AND SETS AUTOMATICALLY SORT THEMSELVES SO THIS IS PERFECT FOR HIGEST AND LOWEST
# nevermind this is really bad to run if you want to still have memory
# probably should have seen that coming considering that its adding every number between absurdly large numbers to a set
# new plan is to keep a list of the ranges and use the difference
# if the difference of the range is higher than the lower range - the id (and thats not negative) then its valid
# that is probably less processing intesive huh

def rangecheck(foodid):
    global ranges
    for item in ranges:
        lower, higher = item
        rangediff = higher - lower
        iddiff = foodid - lower
        if -1 < iddiff <= rangediff:
            return True
    return False


for i,r in enumerate(ranges): # YAAY ENUMERATE
    newrange = list(map(int, r.split("-")))
    ranges[i] = newrange


validcount = 0

for id in foods:
    valid = rangecheck(id)
    if valid:
        validcount += 1

print(f"There are {validcount} fresh foods.")