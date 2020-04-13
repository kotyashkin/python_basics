"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus_nums = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open("5-4.txt" , "r") as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(rus_nums[i[0]] + '  ' + i[1])
    #print(new_file, end='')

with open('5_4_rus.txt', 'w') as file_rus:
    file_rus.writelines(new_file)