import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator:
    for match in re.finditer(r"\d+\.\d{2}", text):
        yield float(match.group())


def sum_profit(text: str, find_nums_func: Callable):
    return sum(find_nums_func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")