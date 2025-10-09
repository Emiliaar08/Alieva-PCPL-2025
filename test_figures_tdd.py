import pytest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.color import FigureColor

class TestFigures:
    @pytest.fixture
    def sample_rectangle(self):
        return Rectangle("синего", 5, 3)
    