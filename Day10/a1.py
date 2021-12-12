with open("input.txt", "r") as file:
    score = 0
    scores = {
        "]": 57,
        "}": 1197,
        ")": 3,
        ">": 25137,
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
                break

            elif char == "[" or char == "{" or char == "(" or char == "<":
                stack.append(char)
            else:
                rightChar = closingSyntax[stack.pop()]
                if rightChar != char:
                    score += scores[char]
                    break

    print(score)
