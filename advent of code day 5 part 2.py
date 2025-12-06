# Day 5

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")
    
emptyindex = inputfile.index("") # grab the index of the separator of the ranges and foods
ranges = inputfile[:emptyindex] # dont need the foods anymore

# New plan
# sort the ranges so that the first value is ascending
# then you can iterate through the ranges list until the ranges stop oerlapping in order to merge them

def conglomeration(rangelist):
    # with the list sorted by the first value the lowest will always be ther first digit of the first range merged
    # the highest you can simply check for each range
    # the buffer range is made up of the lowest and current highest of the overlapping ranges
    # so for each range you check if its highest value is within the range of the next or if it is higher than the next ranges highest
    # once that does not happen anymore, the buffer range is added to the newlist and it starts a new buffer range
    # if its at the end of the list it should stop and not try to compare itself to the next in the list
    # could use a try statement for that
    sortedlist = sorted(rangelist)
    newlist = []
    bufferrange = [0,0]
    startofrange = True
    for i, r in enumerate(sortedlist):
        if startofrange == True:
            bufferrange[0] = r[0]
            startofrange = False
        if r[1] > bufferrange[1]:
            bufferrange[1] = r[1]
        try:
            nextrange = sortedlist[i+1]
        except:
            newlist.append(tuple(bufferrange))
            bufferrange = [0,0]
            startofrange = True
        if startofrange == False:
            if r[1] not in range(nextrange[0],nextrange[1]) and not r[1] >= nextrange[1]:
                newlist.append(tuple(bufferrange))
                bufferrange = [0,0]
                startofrange = True
    return newlist



for i,r in enumerate(ranges): # YAAY ENUMERATE
    newrange = list(map(int, r.split("-")))
    ranges[i] = newrange

conglomeratedlist = conglomeration(ranges)
validcount = 0

for lower, higher in conglomeratedlist:
    difference = higher - lower + 1
    validcount += difference

print(f"There are {validcount} fresh foods.")