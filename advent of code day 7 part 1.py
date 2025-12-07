# Day 7

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")

splitterrows = inputfile[1:]
originindex = inputfile[0].index("S")

# you need a set of indexes the beam is going down
# Then add the origin index and it will check each position in the set in each row it checks
# if thats a splitter, then remove the position being split and add 2 more that are +1 and -1 the index from before

beams = set([originindex])
newbeams = set(list(beams)[:])
splitcount = 0

for row in splitterrows:
    for beam in beams:
        if row[beam] == "^":
            newbeams.remove(beam)
            try:
                newbeams.add(beam+1)
            except:
                pass
            try:
                newbeams.add(beam-1)
            except:
                pass
            splitcount += 1
    beams = set(list(newbeams)[:])

print(f"The final split count was {splitcount}.")