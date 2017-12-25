input = [x for x in open("input-24","r").read().strip().split("\n")]

def get_bridges2(prev, ports):
    lastPort = prev[-1]
    candidates = [port for port in ports if lastPort[1] == port[0] or lastPort[1] == port[1]]
    if not candidates:
        return [prev]
    else:
        res = []
        for port in candidates:
            portIndex = ports.index(port)
            nextPorts = [x for x in ports if x != port]
            nextPrev = [x for x in prev]
            nextPrev.append(port if lastPort[1] == port[    0] else [port[1], port[0]])
            nextBridges = get_bridges2(nextPrev, nextPorts)
            for bridge in nextBridges:
                res.append(bridge)
        return res

input = open("input-24", "r").read().strip().split("\n")
ports = []
for row in [x for x in input]:
    a, b = [int(x) for x in row.split('/')]            
    ports.append([int(a), int(b)])

bridges = get_bridges2([[0,0]], ports)
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
print(max)
#for bridge in get_bridges([(0,0)], ports):
#        bridges.append((len(bridge), sum(a+b for a,b in bridge)))
#part1 = sorted(bridges, key=lambda x: x[1])[-1][1]
#print('part1 %s' % part1)
# part2 = sorted(solution)[-1][1]
# print('part2 %s' % part2)
