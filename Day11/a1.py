import numpy as np

# creates field-array


def getField():


def getNeighbours(pos, field):
    neighbours = list()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if pos[0] + i > -1 and pos[0] + i < field.shape[0] and pos[1] + j > -1 and pos[1] + j < field.shape[1]:
                neighbours.append([pos[0] + i, pos[1] + j])
    return neighbours


field = getField()

count = 0
for step in range(100):
    # 1 increase level of all oct by one
    field += 1

    alreadyFlashed = list()
    while field.flatten()[field.argmax()] > 9:
        for i in range(field.shape[0]):
            for j in range(field.shape[1]):
                if field[i][j] > 9:
                    count += 1
                    field[i][j] = 0
                    alreadyFlashed.append([i, j])
                    neighbours = getNeighbours([i, j], field)
                    for neighbour in neighbours:
                        if not neighbour in alreadyFlashed:
                            field[neighbour[0]][neighbour[1]] += 1

print(count)
