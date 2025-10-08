from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    """
    Класс «Прямоугольник» наследуется от класса «Геометрическая фигура».
    """
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, color_parameter, width_parameter, height_parameter):
        """
        Класс должен содержать конструктор по параметрам «ширина», «высота» и «цвет». В конструкторе создается объект класса «Цвет фигуры» для хранения цвета.
        """
        self.width = width_parameter
        self.height = height_parameter
        self.figure_color = FigureColor()
        self.figure_color.set_color(color_parameter)

    @classmethod
    def get_name(cls):
        return cls.FIGURE_TYPE
    
    def square(self):
        """
        Класс должен переопределять метод, вычисляющий площадь фигуры.
        """
        return self.width*self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_name(),
            self.figure_color.get_color(),
            self.width,
            self.height,
            self.square()
        )