# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
# с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, user_in: str):
        self.user_in = user_in

    def __str__(self):
        return self.user_in

    @classmethod
    def extract(cls, user_in):
        try:
            date = [int(x) for x in user_in.split('-')]
            if len(date) != 3:
                raise ValueError
            return date
        except ValueError:
            print("Неверный формат. Введите строку в формате \"dd-mm-YYYY\" ")

    @staticmethod
    def valid(user_in):
        d = Data.extract(user_in)
        if d is None:
            return False
        if d[1] > 12 or d[1] < 1:
            print("Месяц должен быть в диапазоне - (1- 12)")
            return False
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if d[1] == 2 and d[2] % 4 == 0:
            days_in_month[1] = 29
        else:
            days_in_month[1] = 28
        if d[0] < 0 or d[0] > days_in_month[d[1] - 1]:
            print(f"День в {d[1]} месяце должен быть в диапазоне - (1- {days_in_month[d[1] - 1]})")
            return False
        return True


a = input("Введите строку в формате \"dd-mm-YYYY\"")
if Data.valid(a):
    print("все верно, создаём дату.")
    d1 = Data(a)
    print(f" Ваша дата {d1}")
