"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


file = open('5-5.txt', 'w+')
line = input('Введите числа через пробел: \n')
file.writelines(line)
num = line.split()
print(sum(map(float, num)))
file.close()