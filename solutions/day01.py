def read_day01_01_input_file():
    with open("../inputs/day01_1.txt", "r") as file:
        return [line.split() for line in file.readlines()]


def part_1():
    input_left, input_right = zip(*read_day01_01_input_file())

    sorted_list_left = sorted(map(int, input_left))
    sorted_list_right = sorted(map(int, input_right))

    distances = [abs(i_left - i_right) for i_left, i_right in zip(sorted_list_left, sorted_list_right)]

    return sum(distances)


def part_2():
    input_left, input_right = zip(*read_day01_01_input_file())
    input_left = [int(i) for i in input_left]
    input_right = [int(i) for i in input_right]
    similarity_score = []

    for i in input_left:
        similarity_score.append(i * input_right.count(i))

    return sum(similarity_score)


def main():
    print(part_1())
    print(part_2())

if __name__ == "__main__":
    main()