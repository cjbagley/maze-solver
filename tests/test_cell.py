from unittest import TestCase
from gui.cell import Cell 
from gui.window import Window
from gui.point import Point 

class TestCell(TestCase):
    def test_cell_construction(self):
        win = Window(700, 600)
        cell = Cell(win, Point(20, 300), Point(51, 360)) 

        self.assertEqual(cell._tl_x, 20)
        self.assertEqual(cell._tl_y, 300)
        self.assertEqual(cell._br_x, 51)
        self.assertEqual(cell._br_y, 360)

        self.assertEqual(cell.has_left_wall, True)
        cell.has_left_wall = False
        self.assertEqual(cell.has_left_wall, False)

    def test_get_middle(self):
        win = Window(700, 600)
        cell = Cell(win, Point(20, 200), Point(50, 300)) 
        mid_point = cell.get_middle()
        self.assertEqual(mid_point.x, 35)
        self.assertEqual(mid_point.y, 250)

        cell = Cell(win, Point(17, 20), Point(88, 629)) 
        mid_point = cell.get_middle()
        self.assertEqual(mid_point.x, 52.5)
        self.assertEqual(mid_point.y, 324.5)
