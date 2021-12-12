import ntpath


def day1(inputText):
    inputs = list(map(int, inputText.split("\n")[:-1]))
    count = 0
    for i in range(len(inputs) - 1):
        if inputs[i] < inputs[i + 1]:
            count += 1
    print(f"Day 1 Part 1: {count}")
    count = 0
    for i in range(len(inputs) - 3):
        if inputs[i] < inputs[i + 3]:
            count += 1
    print(f"Day 1 Part 2: {count}")


def day2(inputText):
    inputs = inputText.split("\n")[:-1]
    position = 0
    depth = 0
    for s in inputs:
        command = s.split(" ")
        if command[0] == "forward":
            position += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        else:
            depth -= int(command[1])
    print(f"Day 2 Part 1: {position * depth}")
    position = 0
    depth = 0
    aim = 0
    for s in inputs:
        command = s.split(" ")
        if command[0] == "forward":
            position += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        else:
            aim -= int(command[1])
    print(f"Day 2 Part 2: {position * depth}")


def day3(inputText):
    inputs = inputText.split("\n")[:-1]
    outputs = [0 for _ in range(len(inputs[0]))]
    for s in inputs:
        for i in range(len(s)):
            if s[i] == "1":
                outputs[i] += 1
            else:
                outputs[i] -= 1
    gamma = 0
    epsilon = 0
    for i in range(len(outputs)):
        # Need to reverse output because first char in string is the highest bit in a number
        if outputs[-i - 1] >= 0:
            gamma |= (1 << i)
        else:
            epsilon |= (1 << i)
    print(f"Day 3 Part 1: {gamma * epsilon}")

    inputsCopy = inputs[:]
    bit = 0
    while len(inputsCopy) > 1:
        sum = 0
        for s in inputsCopy:
            if s[bit] == "1":
                sum += 1
            else:
                sum -= 1
        filterBit = "1" if sum >= 0 else "0"
        inputsCopy = list(filter(lambda x: x[bit] == filterBit, inputsCopy))
        bit += 1
    oxygen = int(inputsCopy[0], 2)

    inputsCopy = inputs[:]
    bit = 0
    while len(inputsCopy) > 1:
        sum = 0
        for s in inputsCopy:
            if s[bit] == "1":
                sum += 1
            else:
                sum -= 1
        filterBit = "1" if sum < 0 else "0"
        inputsCopy = list(filter(lambda x: x[bit] == filterBit, inputsCopy))
        bit += 1
    carbon = int(inputsCopy[0], 2)

    print(f"Day 3 Part 2: {oxygen * carbon}")


def day4(inputText):
    boardsStrs = inputText.split("\n\n")
    numbersOriginal = list(map(int, boardsStrs.pop(0).split(",")))
    numbers = numbersOriginal[:]
    boards = []

    for b in boardsStrs:
        board = []
        for r in b.split("\n"):
            for c in r.split(" "):
                if c != "":
                    board.append(int(c))
        boards.append(board)

    boardChecks = [[False for _ in range(25)] for _ in range(len(boards))]
    winner = -1

    currentNumber = 0
    while winner < 0:
        currentNumber = numbers.pop(0)

        for i in range(len(boards)):
            for j in range(len(boards[i])):
                if boards[i][j] == currentNumber:
                    boardChecks[i][j] = True

        for i in range(len(boards)):
            for x in range(5):
                col = True
                for y in range(5):
                    if not boardChecks[i][y * 5 + x]:
                        col = False
                if col:
                    winner = i
            for y in range(5):
                row = True
                for x in range(5):
                    if not boardChecks[i][y * 5 + x]:
                        row = False
                if row:
                    winner = i

    sum = 0
    for i in range(len(boards[winner])):
        if not boardChecks[winner][i]:
            sum += boards[winner][i]

    print(f"Day 4 Part 1: {sum * currentNumber}")

    numbers = numbersOriginal[:]

    boardChecks = [[False for _ in range(25)] for _ in range(len(boards))]
    boardsOut = [False for _ in range(len(boards))]
    loser = -1

    currentNumber = 0
    while loser < 0:
        currentNumber = numbers.pop(0)

        for i in range(len(boards)):
            for j in range(len(boards[i])):
                if boards[i][j] == currentNumber:
                    boardChecks[i][j] = True

        for i in range(len(boards)):
            if not boardsOut[i]:
                for x in range(5):
                    col = True
                    for y in range(5):
                        if not boardChecks[i][y * 5 + x]:
                            col = False
                    if col:
                        boardsOut[i] = True
                        loser = i
                        for j in range(len(boardsOut)):
                            if not boardsOut[j]:
                                loser = -1
                for y in range(5):
                    row = True
                    for x in range(5):
                        if not boardChecks[i][y * 5 + x]:
                            row = False
                    if row:
                        boardsOut[i] = True
                        loser = i
                        for j in range(len(boardsOut)):
                            if not boardsOut[j]:
                                loser = -1
    sum = 0
    for i in range(len(boards[loser])):
        if not boardChecks[loser][i]:
            sum += boards[loser][i]

    print(f"Day 4 Part 2: {sum * currentNumber}")


days = [day1, day2, day3, day4]


def main():
    day = int(input("Select a day: "))
    with open(f"inputs/day{day}.txt", "r") as f:
        inputText = f.read()
        days[day - 1](inputText)


if __name__ == "__main__":
    main()
