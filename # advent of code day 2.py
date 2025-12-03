# advent of code day 2

invalididtotal = 0

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split(",")

for ids in inputfile:
    dashindex = ids.index("-")
    firstid = ids[0:ids.index("-")]
    lastid = ids[ids.index("-") + 1:]
    print("Testing " + str(firstid) + " " + str(lastid) + ". . .")
    for i in range(int(firstid),int(lastid)+1):
        stringi = str(i)
        cache = ""
        cancontinue = False
        for l in range(len(str(i))):
            if not cancontinue:
                cache += stringi[0]
                stringi = stringi[1:]
                if len(stringi) >= len(cache):
                    lendivision = len(stringi) / len(cache)
                    lenint = int(lendivision)
                    if lenint == lendivision:
                        cancontinue = True
                        for w in range(0,len(stringi),len(cache)):
                                if len(cache) > 1:
                                    if stringi[w:w+len(cache)] != cache:

                                        cancontinue = False
                                        break
                                else:
                                    if stringi[w] != cache:
                                        cancontinue = False
                                        break
                        if cancontinue:
                            invalididtotal += int(i)
                            print(f"Adding {i}. . .")
    print(f"The current total of the invalids so far is {invalididtotal}.")