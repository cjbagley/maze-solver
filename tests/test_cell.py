from unittest import TestCase
from gui.cell import Cell 
from gui.window import Window
from gui.point import Point 

class TestCell(TestCase):
    def test_cell_construction(self):
        win = Window(700, 600)
        cell = Cell(win, Point(20, 300), Point(51, 360)) 
        self.assertIsInstance(cell, Cell)
