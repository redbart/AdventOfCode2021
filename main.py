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


days = [day1, day2, day3]


def main():
    day = int(input("Select a day: "))
    with open(f"inputs/day{day}.txt", "r") as f:
        inputText = f.read()
        days[day - 1](inputText)


if __name__ == "__main__":
    main()
