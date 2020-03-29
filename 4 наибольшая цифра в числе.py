input_number = int(input('Введите любое натуральное число: '))
maximum = input_number % 10
input_number = input_number // 10
while input_number > 0:
    if input_number % 10 > maximum:
        maximum = input_number % 10
    input_number = input_number // 10
print(f"Максимальная цифра введённого числа: {maximum}")