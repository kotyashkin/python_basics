"""Реализовать структуру «Рейтинг»,
представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2]."""

list = [7, 5, 3, 3, 2]
print(list)
user_n = int(input('введите натуральное число --> '))
for i in range(len(list)):
    if user_n > list[0]:
        list.insert(0, user_n)
        break
    elif user_n in list:
        i = list.index(user_n)
        list.insert(i+1, user_n)
        break
    elif list[i] > user_n > list[i+1]:
        list.insert(i+1, user_n)
        break
    elif user_n < list[-1]:
        list.append(user_n)
        break

print(list)