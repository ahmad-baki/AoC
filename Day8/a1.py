# returns digits with n amount of lines
def getDigits(n):
    switcher = {
        2: [1],
        3: [7],
        4: [4],
        5: [2, 3, 5],
        6: [6, 9],
        7: [8]
    }
    return switcher[n]


def solutionFound(dic):
    for key in dic:
        if len(dic[key]) > 1:
            return False
    return True


def nOfSameChar(string1, string2):
    n = 0
    for char in string1:
        for char2 in string2:
            if char == char2:
                n += 1
    return n


digitToChars = {
    0: "a, b, c, e, f, g",
    1: "c, f",
    2: "a, c, d, e, g",
    3: "a, c, d, f, g",
    4: "b, c, d, f",
    5: "a, b, d, f, g",
    6: "a, b, d, e, f, g",
    7: "a, c, f",
    8: "a, b, c, d, e, f, g",
    9: "a, b, c, d, f, g"
}

with open("input.txt", "r") as file:
    solution = 0
    for line in file:
        displayDic = {}

        # iterates trhoug digits left
        pointer = 0
        digit = ""
        for i in range(len(line)):
            if(line[i] == ' '):
                displayDic[digit] = getDigits(len(digit))
                digit = ""

            elif(line[i] == '|'):
                pointer = i + 2
                break
            else:
                digit += line[i]

        # iterates through digits right
        targetDic = {}
        digit = ""
        for i in line[pointer:]:
            if(i == ' ' or i == '\n'):
                targetDic[digit] = getDigits(len(digit))
                digit = ""
            else:
                digit += i

        while(not solutionFound(targetDic)):
            # iterates through display
            for key in displayDic:

                # if digit has solution
                if(len(displayDic[key]) == 1):

                    newFoundDigits = {}
                    # iterates through display
                    for key2 in displayDic:
                        if(len(displayDic[key2]) == 1):
                            continue
                        if key2 in newFoundDigits:
                            displayDic[key2] = [newFoundDigits[solutionDigit]]
                            continue

                        nSameChar = nOfSameChar(key, key2)
                        firstDigit = digitToChars[displayDic[key][0]]
                        possibleDigits = getDigits(len(key2))
                        solutionDigit = -1

                        for digit in possibleDigits:
                            if(nOfSameChar(firstDigit, digitToChars[digit]) == nSameChar):
                                if(solutionDigit == -1):
                                    solutionDigit = digit
                                else:
                                    solutionDigit = -1
                                    break

                        if(solutionDigit != -1):
                            displayDic[key2] = [solutionDigit]
                            newFoundDigits[key2] = solutionDigit

                    # iterates through target digits
                    for key2 in targetDic:
                        if(len(targetDic[key2]) == 1):
                            continue
                        if key2 in newFoundDigits:
                            targetDic[key2] = [newFoundDigits[solutionDigit]]
                            continue

                        nSameChar = nOfSameChar(key, key2)
                        firstDigit = digitToChars[displayDic[key][0]]
                        possibleDigits = getDigits(len(key2))
                        solutionDigit = -1

                        for digits in possibleDigits:
                            if(nOfSameChar(firstDigit, digitToChars[digit]) == nSameChar):
                                if(solutionDigit == -1):
                                    solutionDigit = digit
                                else:
                                    solutionDigit = -1
                                    break

                        if(solutionDigit != -1):
                            targetDic[key2] = [solutionDigit]
                            newFoundDigits[key2] = solutionDigit

            # iterates through display
            for key in targetDic:

                # if digit has solution
                if(len(targetDic[key]) == 1):

                    newFoundDigits = {}
                    # iterates through display
                    for key2 in displayDic:
                        if(len(displayDic[key2]) == 1):
                            continue
                        if key2 in newFoundDigits:
                            displayDic[key2] = [newFoundDigits[solutionDigit]]
                            continue

                        nSameChar = nOfSameChar(key, key2)
                        firstDigit = digitToChars[targetDic[key][0]]
                        possibleDigits = getDigits(len(key2))
                        solutionDigit = -1

                        for digits in possibleDigits:
                            if(nOfSameChar(firstDigit, digitToChars[digit]) == nSameChar):
                                if(solutionDigit == -1):
                                    solutionDigit = digit
                                else:
                                    solutionDigit = -1
                                    break

                        if(solutionDigit != -1):
                            displayDic[key2] = [solutionDigit]
                            newFoundDigits[key2] = solutionDigit

                    # iterates through target digits
                    for key2 in targetDic:
                        if(len(targetDic[key2]) == 1):
                            continue
                        if key2 in newFoundDigits:
                            targetDic[key2] = [newFoundDigits[solutionDigit]]
                            continue

                        nSameChar = nOfSameChar(key, key2)
                        firstDigit = digitToChars[targetDic[key][0]]
                        possibleDigits = getDigits(len(key2))
                        solutionDigit = -1

                        for digits in possibleDigits:
                            if(nOfSameChar(firstDigit, digitToChars[digit]) == nSameChar):
                                if(solutionDigit == -1):
                                    solutionDigit = digit
                                else:
                                    solutionDigit = -1
                                    break

                        if(solutionDigit != -1):
                            targetDic[key2] = [solutionDigit]
                            newFoundDigits[key2] = solutionDigit

        for key in targetDic:
            solution += targetDic[key]
    print(solution)
