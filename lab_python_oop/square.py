from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс «Квадрат» наследуется от класса «Прямоугольник».
    """
    FIGURE_TYPE = "Квадрат"

    def __init__(self, color_parameter, side_parameter):
        """
        Класс должен содержать конструктор по параметрам «сторона» и «цвет».
        """
        self.side = side_parameter
        super().__init__(color_parameter, self.side, self.side)

    @classmethod
    def get_name(cls):
        return cls.FIGURE_TYPE
    
    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_name(),
            self.figure_color.get_color(),
            self.side,
            self.square()
        )