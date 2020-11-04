class Rectangle:
    """Класс подсчета S-квадрата"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    """Класс подсчета S-прямоугольника"""
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    """Класс подсчета S-круга"""
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        pi = 3.14
        return pi * self.r ** 2
