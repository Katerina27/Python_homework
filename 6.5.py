# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title='t'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Pen - Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print('Pencil - Запуск отрисовки')


class Handle(Stationery):
    def draw(self):
        print('Handle - Запуск отрисовки')


kancel = Stationery()
kancel.draw()
ruchka = Pen()
ruchka.draw()
karandash = Pencil()
karandash.draw()
marker = Handle()
marker.draw()

