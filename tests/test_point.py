from unittest import TestCase
from gui.point import Point

class TestPoint(TestCase):
    def test_point_construction(self):
       point = Point(3, 200)
       self.assertEqual(point.x, 3)
       self.assertEqual(point.y, 200)
