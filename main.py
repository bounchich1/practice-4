"""New cool python programm"""
import datetime


class NoSuchComman(Exception):
    """the class inherits from the class Exception"""
    pass


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
        return 4
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
    check = ['1', '2', 'help', 'quit']
    quantity = 0
    for i in check:
        if i not in user_command:
            quantity += 1
    if quantity == 4:
        return 0
    return 1


def main() -> None:
    print('Добро пожаловать в программу'
          'оценки задолжности студентов!')
    print('1. Оценка студента исходя из даты сдачи работы \n'
          '2. Список студентов просрочивших сдачу работы \n'
          'help - вывести список действий \n'
          'quit - выйти')
    while True:
        try:
            action = input('Выберите действие: ')
            if 'quit' in action:
                break
            if 'help' in action:
                print('1. Оценка студента исходя из даты сдачи работы \n'
                      '2. Список студентов просрочивших сдачу работы')
            if check_command(action) == 0:
                raise NoSuchComman
            if '1' in action:
                user_deadline = input('Введите дедлайн(в формате DD.MM.YYYY): ')
                from_str_to_datetime(user_deadline)
                user_pass_date = input('Введите дату сдачи работы(в формате DD.MM.YYYY): ')
                result = deadline_score(user_pass_date, user_deadline)
                print(f'Оценка студента: {result}')
            if '2' in action:
                user_deadline = input('Введите дедлайн(в формате DD.MM.YYYY): ')
                from_str_to_datetime(user_deadline)
                user_dict = {}
                print('Вводите фамилии студентов'
                      'и дату сдачи работ'
                      'через пробел \n'
                      'Для окончания ввода используйте - end')
                while True:
                    user_pair = input('Фамилия дата: ')

                    if user_pair == 'end':
                        break
                    else:
                        user_pair = user_pair.split()
                        user_dict[user_pair[0]] = user_pair[1]
                print(f"Список студентов: "
                      f"{''.join(late_list(user_dict, user_deadline))}")
        except ValueError:
            print('Используйте только формат DD.MM.YYYY')
        except NoSuchComman:
            print('Такой команды нет, попробуйте help')


if __name__ == '__main__':
    main()
