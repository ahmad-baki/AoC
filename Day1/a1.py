with open("input.txt", "r") as file:
    prev = 2147483647
    count = 0
    for line in file:
        n = int(line.strip())
        if(n > prev):
            count += 1
        prev = n
    print(count)
