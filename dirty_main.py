from datetime import datetime

from application.salary import *
from application.db.people import *


def show_current_date() -> None:
    """Печатает текущую дату и время."""
    now = datetime.now()
    print(f"Текущая дата и время: {now.strftime('%d.%m.%Y %H:%M:%S')}")


if __name__ == '__main__':
    show_current_date()
    calculate_salary()
    get_employees()
