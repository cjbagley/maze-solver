from unittest import TestCase
from gui.point import Point

class TestPoint(TestCase):
    def test_point_construction(self):
       point = Point(3, 200)
       self.assertEquals(point.x, 3)
       self.assertEquals(point.y, 200)
