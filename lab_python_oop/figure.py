from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный класс «Геометрическая фигура»
    """
    @abstractmethod
    def square(self):
        """
        содержит виртуальный метод для вычисления площади фигуры.
        """
        pass
    @classmethod
    @abstractmethod
    def get_name(cls):
        pass
    @abstractmethod
    def __repr__(self):
        pass