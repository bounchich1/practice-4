"New cool python programm"
import datetime


def from_str_to_datetime(date: str):
    date = date.split('.')
    date = [int(i) for i in date]
    date1 = datetime.datetime(date[2], date[1], date[0])
    return date1


def deadline_score(pass_date: str, deadline_date: str) -> int:
    pass_date = from_str_to_datetime(pass_date)
    deadline_date = from_str_to_datetime(deadline_date)
    delta = int(str(pass_date - deadline_date)[:9].split()[0])
    if delta < 0:
        return 5
    elif delta // 7 == 0:
        return 5
    elif delta // 7 == 1:
        return 4
    elif delta // 7 == 2:
        return 3
    elif delta // 7 == 3:
        return 2
    elif delta // 7 == 4:
        return 1
    elif delta // 7 >= 5:
        return 0


def late_list(grades: dict, deadline_date: str) -> list[str]:
    pass