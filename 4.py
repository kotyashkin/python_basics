

""" 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
print('\nЗадание 1.')
def zp(h, s, b):
    result = h*s+b
    print(f'З/п сотрудника = {result}')
hours = float(input('Выработка в часах: '))
salary = int(input('Ставка (руб.): '))
bonus = int(input('Премия (руб.): '))
zp(hours, salary, bonus)

"""
2
Представлен список чисел. 
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для формирования списка использовать генератор.
"""
print('\nЗадание 2.')
list1 = [46, 10, 15, 32, 25, 0, 28, -115, -50, 90, 6, 12, 2, 1, 9]
list2 = [el for n, el in enumerate(list1) if list1[n - 1] < list1[n]]
print(f'Дан список: {list1}')
print(f'Полученный список: {list2}')


"""
3
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
print('\nЗадание 3.')
print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

"""
4
Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор.
"""
array = [2, 2, 5, 12, 0, 5, -2, 8, 2, 12]
print(f'\nЗадание 4. Дан массив чисел: {array}')
arr2 = [el for el in array if array.count(el) == 1]
print(f'Уникальные элементы данного массива: {arr2}')


"""
5
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce
print('\nЗадание 5.')
array = [el for el in range(100, 1001) if el % 2 == 0]
def multiplex(num1, num2):
    return num1 * num2
print(reduce(multiplex, array))


"""
7
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fibo_gen(). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
"""
from math import factorial
print('\nЗадание 7.')
def fibo_gen(n):
    yield factorial(n)
for el in fibo_gen(15):
    print(el)