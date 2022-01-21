from datetime import date
import calendar

name = "Anastasia"


def task_05_1(name: str) -> str:
    current_day = date.today()
    current_week_day = calendar.day_name[current_day.weekday()]
    return (f"Good day {name}! {current_week_day} is a perfect day " \
            f"to learn some python")


if __name__ == '__main__':
    print(task_05_1(name))
