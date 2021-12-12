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

sum = 0
for i in range(field.shape[0]):
    for j in range(field.shape[1]):
        if(isLowPoint([i, j], field)):
            sum += field[i][j]+1
print(sum)
