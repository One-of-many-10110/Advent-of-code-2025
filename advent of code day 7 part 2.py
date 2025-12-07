# Day 7

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")

splitterrows = inputfile[1:]
originindex = inputfile[0].index("S")

# DO the same thing except you do not use a set, because every path must be calculated, including different ways to get to the same beam location
# Then you can count the number of choices made in order to 
# back to sets because i got another memory error from too many universes in the list :(
# store the number of times that is part of a reality
# GENIUS IDEA
# DICTIONARIES
# have a dictionary with each beam index, and stored alongside it have the number of realities its ine
# and they cant have duplictes
# doesnt matter but neat
# the end number = the number of different realities its in

beams = {originindex : 1}
newbeams = beams.copy()
universecount = 1

for row in splitterrows:
    for beam in beams:
        if row[beam] == "^":
            newbeams.pop(beam)
            try:
                existingrealities = newbeams[beam + 1]
            except:
                existingrealities = 0
            newbeams.update({beam + 1 : existingrealities + (beams[beam])})
            try:
                existingrealities = newbeams[beam - 1]
            except:
                existingrealities = 0
            newbeams.update({beam - 1 : existingrealities + (beams[beam])})
            universecount += 1 * beams[beam]
    beams = newbeams.copy()

print(f"The final universe count was {universecount}.")