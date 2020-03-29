input_seconds = int(input('Введите количество секунд: '))
hours = input_seconds // 3600
remain_seconds = input_seconds - hours * 3600
minutes = remain_seconds // 60
remain_seconds = remain_seconds - minutes * 60
seconds = remain_seconds % 60
print(f"Перевод в формат чч:мм:сс: --> {hours}:{minutes}:{seconds}")