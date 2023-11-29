"""New cool python programm"""
import datetime


def from_str_to_datetime(date: str):
    "function to convert str DD.MM.YYYY to datetime"
    date = date.split('.')
    date = [int(i) for i in date]
    date1 = datetime.datetime(date[2], date[1], date[0])
    return date1


def deadline_score(pass_date: str, deadline_date: str) -> int:
    """function returns student's mark"""
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
    """return a list of students who missed deadline"""
    students = []
    for i in grades:
        deadline_date = from_str_to_datetime(deadline_date)
        pass_date = from_str_to_datetime(grades[i])
        if int(str(pass_date - deadline_date)[:9].split()[0]) > 0:
            students.append(i)
    return students


def check_command(user_command: str) -> int:
    """"The function helps to manage errors"""
    check = ['1', '2', '3', '4', '5', '6', 'help', 'quit']
    quantity = 0
    for i in check:
        if i not in user_command:
            quantity += 1
    if quantity == 8:
        return 0
    return 1


def main() -> None:
    print('Добро пожаловать в программу'
          'оценки задолжности студентов!')
    user_deadline = input('Введите дедлайн(в формате DD.MM.YYYY): \n')
    print('1. Оценка студента исходя из даты сдачи работы \n'
          '2. Список студентов просрочивших сдачу работы')
    action = input('Выберите действие: ')
    while True:
        if 'quit' in action:
            break
        if 'help' in action:
            print('1. Оценка студента исходя из даты сдачи работы \n'
                  '2. Список студентов просрочивших сдачу работы')
