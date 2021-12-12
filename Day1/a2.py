with open("input.txt", "r") as file:
    prev = 2147483647
    count = 0
    i = 1
    summ = [0, 0, 0]
    for line in file:
        n = int(line.strip())
        if i > 2:
            for j in range(3):
                summ[j] += n

            count += 1 if summ[i % 3] > prev else 0
            prev = summ[i % 3]
            summ[i % 3] = 0
        else:
            for j in range(i):
                summ[j] += n
        i += 1

    print(count)
