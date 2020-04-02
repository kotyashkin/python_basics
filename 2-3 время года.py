"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""


list_season = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
dict_season = {'1': 'зима', '2': 'зима', '3': 'весна', '4': 'весна',
'5': 'весна', '6': 'лето', '7': 'лето', '8': 'лето',
'9': 'осень', '10': 'осень', '11': 'осень', '12': 'зима'}
month = input("Введите номер месяца --> ")

print(f'Результат программы через список: {list_season[int(month)-1]}')

print(f'Результат программы через словарь: {dict_season[month]}')