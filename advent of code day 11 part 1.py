# Day 11

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n") 

def routefinder(server):
    global routecount
    outputs = servers[server]
    if outputs[0] == "out":
        routecount += 1
    else:
        for output in outputs:
            routefinder(output)

servers = {}
routecount = 0

for l, line in enumerate(inputfile):
    splitline = line.split(":")
    servers.update({splitline[0]:splitline[1].split()})

routefinder("you")
print(f"The final route count is {routecount}.")
# maybe have a function that calls itself for each different output of a server, starting with the server 'you'
# has a parameter that is the id of the server and will look through its outputs to see if there is an out
# if there is it will add one to the number of ways to get to the out server
# servers put in dictionaries, with their indexes as the server name and the outputs as the items.

