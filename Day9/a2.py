import numpy as np


def isLowPoint(pointer, array):
    value = array[pointer[0]][pointer[1]]

    if pointer[0] - 1 > -1:
        if array[pointer[0] - 1][pointer[1]] <= value:
            return False
    if pointer[1] - 1 > -1:
        if array[pointer[0]][pointer[1] - 1] <= value:
            return False
    if pointer[0] + 1 < array.shape[0]:
        if array[pointer[0] + 1][pointer[1]] <= value:
            return False
    if pointer[1] + 1 < array.shape[1]:
        if array[pointer[0]][pointer[1] + 1] <= value:
            return False
    return True


field = np.array([[]], dtype=np.int32)

# creates field-array
with open("input.txt", "r") as file:
    counter = 0
    for line in file:
        row = np.array([], dtype=np.int32)
        for char in line.strip():
            row = np.append(row, int(char))
        row = row.reshape(1, -1)
        if(counter != 0):
            field = np.append(field, row, axis=0)
        else:
            field = row

        counter += 1

localMins = list()
for i in range(field.shape[0]):
    for j in range(field.shape[1]):
        if(isLowPoint([i, j], field)):
            localMins.append([i, j])

basins = list()
for localMin in localMins:
    finished = False
    basin = list()
    basin.append(localMin)
    while not finished:
        for position in basin:
            finished = True

            # expand basin to the left
            if position[0] - 1 > -1 and field[position[0] - 1][position[1]] != 9:
                if not [position[0] - 1, position[1]] in basin:
                    if field[position[0] - 1][position[1]] > field[position[0]][position[1]]:
                        basin.append([position[0] - 1, position[1]])
                        finished = False

            # expand basin to the right
            if position[0] + 1 < field.shape[0] and field[position[0] + 1][position[1]] != 9:
                if not [position[0] + 1, position[1]] in basin:
                    if field[position[0] + 1][position[1]] > field[position[0]][position[1]]:
                        basin.append([position[0] + 1, position[1]])
                        finished = False

            # expand basin to the top
            if position[1] - 1 > -1 and field[position[0]][position[1] - 1] != 9:
                if not [position[0], position[1]-1] in basin:
                    if field[position[0]][position[1] - 1] > field[position[0]][position[1]]:
                        basin.append([position[0], position[1] - 1])
                        finished = False

            # expand basin to the bottom
            if position[1] + 1 < field.shape[1] and field[position[0]][position[1] + 1] != 9:
                if not [position[0], position[1] + 1] in basin:
                    if field[position[0]][position[1] + 1] > field[position[0]][position[1]]:
                        basin.append([position[0], position[1] + 1])
                        finished = False
    basins.append(len(basin))

sorted_basins = sorted(basins, reverse=True)
print(sorted_basins[0] * sorted_basins[1] * sorted_basins[2])
