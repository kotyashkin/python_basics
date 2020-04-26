"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма: {self.a + other.a} + {self.b + other.b}*i'

    def __mul__(self, other):
        return f'Произведение: {self.a*other.a - self.b*other.b} + {self.a*other.b + self.b*other.a}*i'

    def __str__(self):
        return f'{self.a} + {self.b}*i'


c1 = ComplexNumber(3, -2)
c2 = ComplexNumber(13, -5)
print(f'Первое комплексное число: {c1}')
print(f'Второе комплексное число: {c2}')
print(c1 + c2)
print(c1 * c2)