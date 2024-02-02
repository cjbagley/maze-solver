from unittest import TestCase
from gui.cell import Cell 

class TestCell(TestCase):
    def test_cell_construction(self):
        cell = Cell() 
        self.assertIsInstance(cell, Cell)