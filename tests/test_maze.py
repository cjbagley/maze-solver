from unittest import TestCase
from gui.maze import Maze 
from gui.window import Window
from gui.point import Point 

class TestMaze(TestCase):
    def test_maze_construction(self):
        win = Window(700, 600)
        starting_point = Point(10, 100)
        Maze(
            window=win,
            starting_point=starting_point,
            num_rows=3,
            num_cols=4,
            cell_size_x=4,
            cell_size_y=5
        )
