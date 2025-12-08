# Day 8

from itertools import combinations

from math import sqrt

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n")

def getsmallestconnection(dist, circ):
    for distance in dist:
        A, B = dist[distance]
        for c, circuit in enumerate(circ):
            if A in circuit:
                Aindex = c
            if B in circuit:
                Bindex = c
        if Aindex != Bindex:
            return distance, Aindex, Bindex

for l, line in enumerate(inputfile):
    inputfile[l] = list(map(int, line.split(",")))
inputlength = len(inputfile)

circuits = []
for i in range(inputlength):
    circuits.append([inputfile[i]])


distances = {}
for Apoint,Bpoint in combinations(inputfile, 2):
    distance = sqrt((Apoint[0] - Bpoint[0])**2 + (Apoint[1] - Bpoint[1])**2 + (Apoint[2] - Bpoint[2])**2)
    distances.update({distance : (Apoint,Bpoint)})

distances = dict(sorted(distances.items()))

for i in range(1000):
    lowest = list(distances)[i]
    for c, circuit in enumerate(circuits):
        if distances[lowest][0] in circuit:
            Acircuit = c
    for c, circuit in enumerate(circuits):
        if distances[lowest][1] in circuit:
            Bcircuit = c
    if Acircuit != Bcircuit:
        circuits[Acircuit] = circuits[Acircuit] + circuits[Bcircuit]
        circuits.remove(circuits[Bcircuit])

# so look through the distances dict until you find the shortest distance with a point a in one circuit and a point B in the other
# keep that distance handy for later
# merge the two lists

while len(circuits) != 1:
    connect, A, B= getsmallestconnection(distances, circuits)
    circuits[A] += circuits[B]
    circuits.remove(circuits[B])
print(str(distances[connect][0][0] * distances[connect][1][0] ))