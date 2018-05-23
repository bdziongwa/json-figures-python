import pygame
from abc import abstractmethod, ABC

# Klasa bazowa figur
# zawiera pola x i y
# oraz metodę set_color()
class Figure(ABC):
    color = (0, 0, 0)
    x = 0
    y = 0

    def __init__(self, x=0, y=0, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def draw(self, screen):
        pass


class Circle(Figure):
    radius = 40

    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.radius)


# Klasa Point dziedziczy z klasy Circle
# tworzymy koło o promieniu równym 1
class Point(Circle):
    def __init__(self, x, y, color=pygame.Color(255, 255, 255)):
        super().__init__(x, y, color, 1)


class Rectangle(Figure):
    width = 0
    height = 0

    def __init__(self, x, y,  width, height, color=pygame.Color(255, 255, 255)):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])


# Klasa Square dziedziczy z klasy Rectangle
# tworzymy prostokąt o równych bokach
class Square(Rectangle):
    size = 40

    def __init__(self, x, y, color, size):
        super().__init__(x, y, size, size, color)
        self.size = size


class Polygon(Figure):
    points = []

    def __init__(self, color, points,  x=0, y=0):
        super().__init__(0, 0, color)
        self.points = points

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)
