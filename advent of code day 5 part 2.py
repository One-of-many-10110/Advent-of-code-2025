# Day 5

with open("example.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")
    
emptyindex = inputfile.index("") # grab the index of the separator of the ranges and foods
ranges = inputfile[:emptyindex] # dont need the foods anymore

# So this would be really easy with what i did before
# so maybe see if in the ranges list the lowest index is inside the range of another
# then if it is make that other ranges lower value and the first ranges higher value merge
# that could work

def conglomeration(rangelist):
    newlist = rangelist
    previouslist = []
    while newlist != previouslist:
        previouslist = newlist[:]
        for t, thing in enumerate(newlist):
            for otherthing in newlist:
                if otherthing[0] in range(thing[0],thing[1]) and otherthing != thing:
                    newlist.remove(otherthing)
                    if otherthing[1] > thing[1]:
                        newlist.remove(thing)
                        newlist.append([thing[0],otherthing[1]])
                    break
            if len(previouslist) != len(newlist):
                break
    return newlist



for i,r in enumerate(ranges): # YAAY ENUMERATE
    newrange = list(map(int, r.split("-")))
    newrange[1] += 1
    ranges[i] = newrange

conglomeratedlist = conglomeration(ranges)
validcount = 0

for item in conglomeratedlist:
    lower, higher = item
    difference = higher - lower
    validcount += difference

print(f"There are {validcount} fresh foods.")