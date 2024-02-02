from unittest import TestCase
from gui.line import Line
from gui.point import Point

class TestLine(TestCase):
    def test_line_construction(self):
        try:
            point_a = Point(10, 20)
            point_b = Point(40, 20)
            line = Line(point_a, point_b)
        except:
            self.fail("Line could not be constructed")
        
        self.assertIsInstance(line, Line)