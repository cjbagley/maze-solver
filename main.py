#!/usr/bin/env python
import sys
from gui.maze import Maze
from gui.window import Window
from gui.point import Point

def main() -> int:
    """Maze solver"""
    win = Window(820, 820)
    Maze(
            window=win,
            starting_point=Point(10,10),
            num_rows=8,
            num_cols=8,
            cell_size_x=100,
            cell_size_y=100,
    )

    win.wait_for_close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
