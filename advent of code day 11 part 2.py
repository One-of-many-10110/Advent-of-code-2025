# Day 11

from functools import cache

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n") 

@cache
def routefinder(server,fft,dac):
    outputs = servers[server]
    if outputs[0] == "out" and fft == True and dac == True:
        return 1
    elif outputs[0] == "out":
        return 0
    else:
        returnvalue = 0
        for output in outputs:
            if output == "fft":
                returnvalue += routefinder(output,True,dac)
            elif output == "dac":
                returnvalue += routefinder(output,fft,True)
            else:
                returnvalue += routefinder(output,fft,dac)
        return returnvalue

servers = {}

for l, line in enumerate(inputfile):
    splitline = line.split(":")
    servers.update({splitline[0]:splitline[1].split()})

print(f"The final route count is {routefinder("svr", False, False)}.")


