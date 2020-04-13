"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""


file = open('5-2.txt', 'r')
lines = file.readlines()
print(f'Количество строк в файле - {len(lines)}\n')
i = 1
for line in lines:
    line = line.split()
    print(f'Строка {i} имеет {len(line)} слов(а)\n')
    i += 1
file.close()