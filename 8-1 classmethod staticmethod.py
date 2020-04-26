"""
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
class Data:
    def __init__(self, dmy):
        self.dmy = str(dmy)
    @classmethod
    def extract(cls, dmy):
        date = []
        for i in dmy.split('-'):
            date.append(i)
        print(int(date[0]), int(date[1]), int(date[2]))
    @staticmethod
    def valid(d, m, y):
        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 2020 >= y >= 0:
                    return f'Дата корректна'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

print(Data.valid(22, 4, 2022))
print(Data.valid(22, 13, 2020))
print(Data.valid(32, 4, 2020))
print(Data.valid(22, 4, 2020))
Data.extract('22-04-2020')