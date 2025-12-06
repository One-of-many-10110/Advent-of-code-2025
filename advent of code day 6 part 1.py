# Day 6

from math import prod

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")

numbers, operators = inputfile[:-1], inputfile[-1].split(" ")
for i, number in enumerate(numbers):
    numbers[i] = number.split(" ")
for i in range(len(numbers)):
    while True:
        try:
            numbers[i].remove("")
        except:
            break

while True:
    try:
        operators.remove("")
    except:
        break

for i, number in enumerate(numbers):
    numbers[i] = tuple(map(int, number))

finaltotal = 0

for i in range(len(numbers[0])):
    numberbuffer = []
    operator = operators[i]
    for number in numbers:
        numberbuffer.append(number[i])
    if operator == "+":
        output = sum(numberbuffer)
        finaltotal += output
    else:
        output = prod(numberbuffer)
        finaltotal += output
print(f"The final total was {finaltotal}.")