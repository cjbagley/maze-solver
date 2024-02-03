#!/usr/bin/env python
import sys
from gui.maze import Maze
from gui.window import Window
from gui.line import Line
from gui.point import Point
from gui.cell import Cell 

def main() -> int:
    """Maze solver"""
    win = Window(800, 800)
    maze = Maze(
            window=win,
            starting_point=Point(0,0),
            num_rows=4,
            num_cols=10,
            cell_size_x=10,
            cell_size_y=10,
    )
    # cella = Cell(win, Point(10, 10), Point(100, 100))
    # cella.has_right_wall = False
    # cella.draw()
    #
    # cellb = Cell(win, Point(100, 10), Point(200, 100))
    # cellb.has_left_wall = False
    # cellb.has_bottom_wall = False
    # cellb.draw()
    # cellb.draw_move(cella, True)
    #
    # cellc = Cell(win, Point(100, 100), Point(200, 200))
    # cellc.has_top_wall = False
    # cellc.draw()
    # cellc.draw_move(cellb, True)

    win.wait_for_close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
