from itertools import pairwise, count, combinations


def read_day02_1_input_file():
    with open("../inputs/day02_1.txt", "r") as file:
        return [line.split() for line in file.readlines()]


def report_is_safe(report: list[int]) -> bool:
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False
    level_differences = [abs(x - y) for x, y in pairwise(report)]
    if not all(1 <= diff <= 3 for diff in level_differences):
        return False
    return True


def part_1():
    reports_raw = read_day02_1_input_file()

    reports = []

    for report_raw in reports_raw:
        reports.append([int(level_raw) for level_raw in report_raw])

    return [report_is_safe(report) for report in reports].count(True)


def part_2():
    reports_raw = read_day02_1_input_file()

    reports = []
    for report_raw in reports_raw:
        reports.append([int(level_raw) for level_raw in report_raw])

    safe_reports = 0

    for report in reports:
        if report_is_safe(report):
            safe_reports += 1
        else:
            for report_variant in combinations(report, len(report) - 1):
                if report_is_safe(list(report_variant)):
                    safe_reports += 1
                    break

    return safe_reports


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
