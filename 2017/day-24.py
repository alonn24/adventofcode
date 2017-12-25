def get_bridges(prev, ports):
    lastPort = prev[-1]
    candidates = [port for port in ports if lastPort[1] == port[0] or lastPort[1] == port[1]]
    bridges = []
    if not candidates:
        bridges.append(prev)
    else:
        for port in candidates:
            portIndex = ports.index(port)
            nextPorts = [x for x in ports if x != port]
            nextPrev = [x for x in prev]
            nextPrev.append(port if lastPort[1] == port[    0] else [port[1], port[0]])
            nextBridges = get_bridges(nextPrev, nextPorts)
            for bridge in nextBridges:
                bridges.append(bridge)
    return bridges

input = open("day-24.input", "r").read().strip().split("\n")
ports = list(map(lambda x: [int(y) for y in x.split('/')], input))
bridges = get_bridges([[0,0]], ports)

maxVal = 0
maxBridge = []
for bridge in bridges:
    sumVal = sum(a+b for a, b in bridge)
    lengthVal = len(bridge)
    if (len(bridge) > len(maxBridge) or 
            (len(bridge) == len(maxBridge) and sumVal > maxVal)):
        maxVal = sumVal
        maxBridge = bridge
print(maxVal)
