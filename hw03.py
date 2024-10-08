from collections import defaultdict
from sys import argv
from pathlib import Path


def parse_log_line(line: str) -> dict:
    log = line.strip().split(" ", maxsplit=3)
    return {
        "date": log[0],
        "time": log[1],
        "level": log[2],
        "info": log[3]
    }


def load_logs(file_path: str) -> list:

    with open(file_path, "r", encoding="utf-8") as log_file:
        logs = [parse_log_line(log) for log in log_file.readlines()]

    return logs


def filter_logs_by_level(logs: list, level: str) -> filter:
    return filter(lambda log: log["level"] == level, logs)


def count_logs_by_level(logs: list) -> defaultdict:

    counter = defaultdict(int)
    
    for log in logs:
        counter[log["level"]] += 1

    return counter


def display_log_counts(counter: dict):

    col1 = "Рівень логування"
    col2 = "Кількість"

    width_col1 = len(col1)
    width_col2 = len(col2)

    vert_sep = "|"
    hor_sep = "-"

    print(f"{col1:<{width_col1}} {vert_sep} {col2:>{width_col2}}")
    print(f"{hor_sep * (width_col1 + 1)}{vert_sep}{hor_sep * (width_col2 + 1)}")

    for log, count in counter.items():
        print(f"{log:<{width_col1}} {vert_sep} {count:<{width_col2}}")


def display_log_details(logs: list, level: str):

    print(f"\nДеталі логів для рівня '{level}':")

    for log in filter_logs_by_level(logs, level):
        print(f'{log["date"]} {log["time"]} - {log["info"]}')


def main():

    try:
        path_to_file = Path(argv[1])
        logs = load_logs(path_to_file)
        display_log_counts(count_logs_by_level(logs))
        if len(argv) > 2:
            display_log_details(logs, argv[2].upper())
    except FileNotFoundError as error:
        print(error)
    except IndexError:
        print("[Error] There is an error while reading file")


if __name__ == "__main__":
    main()