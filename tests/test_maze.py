from unittest import TestCase
from gui.maze import Maze 
from gui.window import Window
from gui.point import Point 

class TestMaze(TestCase):
    def test_maze_construction(self):
        win = Window(800, 800)
        starting_point = Point(0, 0)
        rows = 3
        cols = 4
        m = Maze(
            window=win,
            starting_point=starting_point,
            num_rows=rows,
            num_cols=cols,
            cell_size_x=4,
            cell_size_y=5
        )
        self.assertEqual(len(m._Maze__cells), cols)
        self.assertEqual(len(m._Maze__cells[0]), rows)
        entrance = m._Maze__cells[0][0]
        self.assertEqual(entrance.has_top_wall, False)
        exit = m._Maze__cells[cols-1][rows-1]
        self.assertEqual(exit.has_bottom_wall, False)
        
        rows = 1
        cols = 9
        m = Maze(
            window=win,
            starting_point=starting_point,
            num_rows=rows,
            num_cols=cols,
            cell_size_x=10,
            cell_size_y=20
        )
        self.assertEqual(len(m._Maze__cells), cols)
        self.assertEqual(len(m._Maze__cells[0]), rows)
        entrance = m._Maze__cells[0][0]
        self.assertEqual(entrance.has_top_wall, False)
        exit = m._Maze__cells[cols-1][rows-1]
        self.assertEqual(exit.has_bottom_wall, False)
