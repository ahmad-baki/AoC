import numpy as np


def getNeighbours(cave, allCaves):
    neighbours = list()
    for i in allCaves:
        if i[0] == cave:
            neighbours.append(i[1])
        elif i[1] == cave:
            neighbours.append(i[0])
    return neighbours


def canVisitCave(cave, list):
    if cave == "start":
        return False

    if not cave in list:
        return True

    if len(np.unique(list)) != len(list):
        return False
    # for i in range(len(list)):
    #     for j in range(len(list)):
    #         if i == j:
    #             continue
    #         if list[i] == list[j]:
    #             return False
    return True


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


# system = [
#     ["start", "A"],
#     ["start", "b"],
#     ["A", "c"],
#     ["A", "b"],
#     ["b", "d"],
#     ["A", "end"],
#     ["b", "end"]
# ]

nextCaves = list()
count = 0
nextCaves.append(["start", ["start"]])
while nextCaves.__len__() > 0:
    nextCave = nextCaves.pop()
    nextCaveNeigbours = getNeighbours(nextCave[0], system)
    for i in nextCaveNeigbours:
        if i == "end":
            count += 1
        elif i[0].islower():
            if not canVisitCave(i, nextCave[1]):
                continue

            lowerCases = list()
            for j in nextCave[1]:
                lowerCases.append(j)

            lowerCases.append(i)
            nextCaves.append([i, lowerCases])
        else:
            nextCaves.append([i, nextCave[1]])
print(count)
