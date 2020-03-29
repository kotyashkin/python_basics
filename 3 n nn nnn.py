input_n = int(input('Введите n - целое число от 1 до 9 (включительно): '))
while input_n > 9 or input_n < 1:
    input_n = int(input("Нужно ввести целое число от 1 до 9! Попробуйте заново: "))
nnn = input_n * 123
print(f"Сумма n+nn+nnn равна: {nnn}")