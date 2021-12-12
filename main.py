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


days = [day1, day2]


def main():
    day = int(input("Select a day: "))
    with open(f"inputs/day{day}Input.txt", "r") as f:
        inputText = f.read()
        days[day - 1](inputText)


if __name__ == "__main__":
    main()
