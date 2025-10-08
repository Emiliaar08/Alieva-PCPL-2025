from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    """
    Класс «Круг» наследуется от класса «Геометрическая фигура».
    """
    FIGURE_TYPE = "Круг"

    def __init__(self, color_parameter,  radius_parameter):
        """
        Класс должен содержать конструктор по параметрам «радиус» и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета.
        """
        self.radius = radius_parameter
        self.figure_color = FigureColor()
        self.figure_color.set_color(color_parameter)

    @classmethod
    def get_name(cls):
        return cls.FIGURE_TYPE

    def square(self):
        """
        Класс должен переопределять метод, вычисляющий площадь фигуры.
        """
        return math.pi*(self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_name(),
            self.figure_color.get_color(),
            self.radius,
            self.square()
        )