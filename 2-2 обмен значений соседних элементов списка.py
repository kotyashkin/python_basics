list = []
i = int(input('Сколько будет элементов в списке? '))

for j in range(0, i):
    j = input(f"введите {j+1}-й элемент: ")
    list.append(j)
print(f"Введённый список: {list}")

j = 0
for i in range(int(len(list)/2)):
    list[j], list[j+1] = list[j+1], list[j]
    j += 2
print(f"Список с обменом значений соседних элементов: {list}")