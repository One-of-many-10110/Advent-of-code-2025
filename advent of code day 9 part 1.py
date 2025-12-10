# Day 9

from itertools import combinations

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n") 

for i, line in enumerate(inputfile):
    inputfile[i] = list(map(int, line.split(",")))

highestarea = [0, ([0,0],[0,0])]
for A, B in combinations(inputfile, 2):
    area = (abs(A[0]-B[0]) + 1) * (abs(A[1]-B[1]) + 1)
    if area > highestarea[0]:
        highestarea = [area,(A,B)]
print(str(highestarea))