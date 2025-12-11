# Day 11

with open("input.txt",mode="r",encoding="utf-8-sig") as file:
    inputfile = file.read().split("\n") 

def routefinder(server,fft,dac):
    global routecount
    outputs = servers[server]
    if outputs[0] == "out" and fft == True and dac == True:
        routecount += 1
    elif outputs[0] == "out":
        pass
    else:
        for output in outputs:
            if output == "fft":
                routefinder(output,True,dac)
            elif output == "dac":
                routefinder(output,fft,True)
            else:
                routefinder(output,fft,dac)

servers = {}
routecount = 0

for l, line in enumerate(inputfile):
    splitline = line.split(":")
    servers.update({splitline[0]:splitline[1].split()})

routefinder("svr", False, False)
print(f"The final route count is {routecount}.")


