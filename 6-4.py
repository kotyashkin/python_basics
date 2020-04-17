"""
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn_right(self):
        return f'{self.name} повернула направо'
    def turn_left(self):
        return f'{self.name} повернула налево'
    def show_speed(self):
        return f'Скорость машины {self.name} составляет {self.speed} км/ч.'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость TownCar {self.name} - {self.speed} км/ч, что выше допустимого значения (60 км/ч)!!!'
        else:
            return f'Скорость TownCar {self.name} - {self.speed} км/ч.'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость WorkCar {self.name} - {self.speed} км/ч, что выше допустимого значения (40 км/ч)!!!'
        else:
            return f'Скорость WorkCar {self.name} - {self.speed} км/ч.'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

ferrari = SportCar(320, 'Красный', 'Ferrari', False)
gaz24 = TownCar(60, 'Серый', 'Газ 24', False)
uaz452 = WorkCar(65, 'Белый', 'УАЗ "буханка"', False)
uaz_P = PoliceCar(100, 'Бело-синий', 'Уаз Патриот', True)

print(f'{ferrari.go()}, цвет машины - {ferrari.color}. Класс - SportCar.')
print(ferrari.show_speed())
print(f'{ferrari.is_police} - булево значение на вопрос "является ли машина полицейской?"')
print(ferrari.turn_left())
print(ferrari.stop())

print(f'\n{gaz24.go()}, цвет машины - {gaz24.color}. {gaz24.show_speed()}')
print(f'{gaz24.turn_right()}, {gaz24.stop()}.')
print(f'{gaz24.is_police} - булево значение на вопрос "является ли машина полицейской?"')

print(f'\n{uaz452.go()}, цвет машины - {uaz452.color}. {uaz452.show_speed()}')
print(f'{uaz452.is_police} - булево значение на вопрос "является ли машина полицейской?"')

print(f'\n{uaz_P.go()}, цвет машины - {uaz_P.color}. {uaz_P.show_speed()}')
print(f'{uaz_P.is_police} - ответ на "является ли машина полицейской?"')