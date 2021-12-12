commands = {
    "forward": [1, 0],
    "down": [0, 1],
    "up": [0, -1]
}

with open("input.txt", "r") as file:
    position = [0, 0]
    for line in file:
        command = ""
        for i in range(len(line.strip())):
            if line[i] != " ":
                command += line[i]
            else:
                position[0] += commands[command][0] * int(line[i+1:])
                position[1] += commands[command][1] * int(line[i+1:])
                break
    print(position[0] * position[1])
