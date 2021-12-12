def getNeighbours(cave, allCaves):
    neighbours = list()
    for i in allCaves:
        if i[0] == cave:
            neighbours.append(i[1])
        elif i[1] == cave:
            neighbours.append(i[0])
    return neighbours


system = [
    ["VJ", "nx", ],
    ["start", "sv"],
    ["nx", "UL"],
    ["FN", "nx"],
    ["FN", "zl"],
    ["end", "VJ"],
    ["sv", "hi"],
    ["em", "VJ"],
    ["start", "hi"],
    ["sv", "em"],
    ["end", "zl"],
    ["zl", "em"],
    ["hi", "VJ"],
    ["FN", "em"],
    ["start", "VJ"],
    ["jx", "FN"],
    ["zl", "sv"],
    ["FN", "sv"],
    ["FN", "hi"],
    ["nx", "end"]]

nextCaves = list()
count = 0
nextCaves.append(["start", ["start"]])
while nextCaves.__len__() > 0:
    nextCave = nextCaves.pop()
    nextCaveNeigbours = getNeighbours(nextCave[0], system)
    for i in nextCaveNeigbours:
        if not i in nextCave[1]:
            if i == "end":
                count += 1
            elif i[0].islower():
                lowerCases = list()
                for j in nextCave[1]:
                    lowerCases.append(j)

                lowerCases.append(i)
                nextCaves.append([i, lowerCases])
            else:
                nextCaves.append([i, nextCave[1]])
print(count)
