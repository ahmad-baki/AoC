commands = {
    "down": 1,
    "up": -1
}

with open("input.txt", "r") as file:
    position = [0, 0]
    aim = 0
    for line in file:
        command = ""
        for i in range(len(line.strip())):
            if line[i] != " ":
                command += line[i]
            else:
                if command == "forward":
                    position[0] += int(line[i+1:])
                    position[1] += int(line[i+1:]) * aim
                else:
                    aim += commands[command] * int(line[i+1:])
                break
    print(position[0] * position[1])
