# advent of code day 3

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")

numbertotal = 0

for bank in inputfile:
    currenthighest = 0
    secondhighest = 0
    banklength = len(bank)
    for i in range(banklength):
        # so you put the largest number you find in the first position no matter what EXCEPT if it is the last digit, in which case it should become the second digit
        # then look at the stuff after that digit to see the next largest digit 
        if int(bank[i]) > currenthighest and i != banklength - 1:
            currenthighest = int(bank[i])
            secondhighest = 0
        elif int(bank[i]) > secondhighest:
            secondhighest = int(bank[i])
    finalnumber = str(currenthighest) + str(secondhighest)
    print(f"Ended with the number {finalnumber}.")
    numbertotal += int(finalnumber)
print(f"The final total is {numbertotal}.")