"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from lab5.my_library import task5_1, task5_2, task5_3, task5_4, task5_5, task5_6, task5_7



def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:
                s = input('Введите строку с запятой: ')

                print(f"Количество букв 'н' после первой запятой: {task5_1(s)}")

            case 2:
                text = input('Введите текст: ')

                task5_2(text)

            case 3:
                text = input("Введите текст: ")
                k = int(input("Введите номер буквы для замены (начиная с 1): "))
                char = input("Введите символ для замены: ")

                print(f"Изменённый текст: {task5_3(text, k, char)}")

            case 4:
                text = input('введите текст: ')

                print(task5_4(text))

            case 5:
                snils = input("Введите номер СНИЛС в формате XXX-XXX-XXX XX: ")

                task5_5(snils)

            case 6:

                print(task5_6())

            case 7:
                s = input("Введите математическое выражение с **: ")
                print(task5_7(s))

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break


