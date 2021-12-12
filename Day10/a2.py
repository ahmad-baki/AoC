with open("input.txt", "r") as file:
    scoresList = list()
    scores = {
        "]": 2,
        "}": 3,
        ")": 1,
        ">": 4,
    }
    closingSyntax = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">",
    }
    for line in file:
        stack = []
        score = 0
        for char in line:
            if char == '\n':
                if len(stack) != 0:
                    while len(stack) != 0:
                        rightChar = stack.pop()
                        score *= 5
                        score += scores[closingSyntax[rightChar]]
                    scoresList.append(score)

            elif char == "[" or char == "{" or char == "(" or char == "<":
                stack.append(char)
            else:
                rightChar = closingSyntax[stack.pop()]
                if rightChar != char:
                    break

    sortedListScores = sorted(scoresList, reverse=True)
    index = int((len(sortedListScores)-1)/2)
    print(sortedListScores[index])
