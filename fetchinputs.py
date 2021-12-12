import requests
import datetime


def main():
    token = input("Enter session token: ")
    today = datetime.datetime.today()
    day = today.day
    if today.hour < 7:
        day -= 1

    for i in range(day):
        r = requests.get(f"https://adventofcode.com/2021/day/{i + 1}/input", cookies={"session": token})
        with open(f"inputs/day{i + 1}.txt", "wb+") as f:
            f.write(r.content)
        print(f"Got day {i + 1} successfully")


if __name__ == "__main__":
    main()
