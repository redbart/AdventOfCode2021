def day1():
    print("Hello world!")


days = [day1]


def main():
    day = int(input("Select a day: "))
    days[day]()


if __name__ == "__main__":
    main()
