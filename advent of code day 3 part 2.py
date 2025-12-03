# advent of code day 3

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")

numbertotal = 0

def getindex(digitlist,item,positionsleft):
    listlength = len(digitlist)
    # go through the list from the first position to the end
    # if the item is more than one of the list items, and there is enough digits left in the bank to fill the rest of the spots then it replaces it
    # otherwise continue to the next item and if you hit the end of the list return 1000
    # if a position is found for it to be, then return that index and other stuff idk focus on this for now
    for i in range(listlength):
        if item > digitlist[i] and (listlength - (i+1) ) <= positionsleft:
            return i
    return 1000

for bank in inputfile:
    finalnumber = ""
    highestdigits = [0,0,0,0,0,0,0,0,0,0,0,0]
    banklength = len(bank)
    for i in range(banklength):
        # function to do all the hard stuff, but it will return an index, or 1000 if there was no correct index
        # so check for that
        # oh yeah also figure out the number of digits left in the bank by doing the length minus the current position + 1
        # AND REMEMBER TO SET ALL THE DIGITS AFTER TO 0 FOR THE LOVE OF GOD
        remainingdigits = banklength - (i+1)
        indexinsertion = getindex(highestdigits,int(bank[i]),remainingdigits)
        if indexinsertion != 1000:
            highestdigits[indexinsertion] = int(bank[i])
            for l in range(indexinsertion+1,12):
                highestdigits[l] = 0
    for item in highestdigits:
        finalnumber += str(item)
    print(f"Ended with the number {finalnumber}.")
    numbertotal += int(finalnumber)
print(f"The final total is {numbertotal}.")