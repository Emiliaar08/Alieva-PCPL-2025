
class FigureColor:
    """
    Класс «Цвет фигуры»
    """

    def __init__(self):
        self._color = None

    def get_color(self):
        """
        Get-аксессор
        """
        return self._color

    def set_color(self, value):
        """
        Set-аксессор
        """
        self._color = value