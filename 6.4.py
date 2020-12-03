# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'the car {self.name} is moving')

    def stop(self):
        print(f'the car {self.name} stopped')

    def turn(self, turn):
        if turn == 0:
            print(f'the car {self.name} turned right')
        else:
            print(f'the car {self.name} turned left')

    def show_speed(self):
        print(f'current speed of car {self.name} is {self.speed}')

    def police(self):
        if self.is_police == 0:
            print(f'the car {self.name} is not a police car')
        else:
            print(f'the car {self.name} is a police car')


class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print (f'the car {self.name} exceed speed limits by {self.speed - 60}')
        else:
            print(f'current speed of car {self.name} is {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'the car {self.name} exceed speed limits by {self.speed - 40}')
        else:
            print(f'current speed of car {self.name} is {self.speed}')


class PoliceCar(Car):
    pass

police = PoliceCar(80, 'black', "Toyota", True)
police.police()
police.go()
police.show_speed()
police.turn(1)
police.stop()

town = TownCar(80, 'blue', "Mazda", False)
town.police()
town.go()
town.show_speed()
town.turn(1)
town.stop()

sport = SportCar(150, 'red', "Ferrari", False)
sport.police()
sport.go()
sport.show_speed()
sport.turn(0)
sport.stop()

work = WorkCar(50, 'white', "Mercedez", False)
work.police()
work.go()
work.show_speed()
work.turn(0)
work.stop()


