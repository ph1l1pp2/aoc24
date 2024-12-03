import re


def read_day03_1_input_file():
    with open("../inputs/day03_1.txt", "r") as file:
        return file.read()


def mul(a, b):
    return a * b


def part_1():
    day3_input = read_day03_1_input_file()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, day3_input)

    results = [int(a) * int(b) for a, b in matches]

    return sum(results)


def part_2():
    day3_input = read_day03_1_input_file()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))"
    matches = re.findall(pattern, day3_input)

    on = True
    results = []
    for a, b, do, dont in matches:
        if do:
            on = True
        elif dont:
            on = False
        elif on:
            results.append(int(a) * int(b))

    return sum(results)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
