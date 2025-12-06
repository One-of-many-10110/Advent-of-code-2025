# Day 6

from math import prod

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")

numbers, operators = inputfile[:-1], inputfile[-1].split(" ")

emptyindexes = []

listlength = len(numbers)
for i in range(len(numbers[0])):
    bufferlist = ""
    for number in numbers:
        bufferlist += number[i]
    if bufferlist == " " * listlength:
        emptyindexes.append(i)

while True:
    try:
        operators.remove("")
    except:
        break

finaltotal = 0
columnnumbers = []
numberbuffer = ""

for i in range(len(numbers[0])):
    if i not in emptyindexes:
        for number in numbers:
            numberbuffer += number[i]
        numberbuffer += "-"
    else:
        columnnumbers.append(numberbuffer[:-1])
        numberbuffer = ""
if numberbuffer != "":
    columnnumbers.append(numberbuffer[:-1])

for c, column in enumerate(columnnumbers):
    col = tuple(map(int, column.split("-")))
    operator = operators[c]
    if operator == "+":
        finaltotal += sum(col)
    else:
        finaltotal += prod(col)

print(f"The final total was {finaltotal}.")