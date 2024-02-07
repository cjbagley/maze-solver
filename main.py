#!/usr/bin/env python
import sys
from gui.maze import Maze
from gui.window import Window
from gui.point import Point

def main() -> int:
    """Maze solver"""
    win = Window(820, 820)
    m = Maze(
            window=win,
            starting_point=Point(10,10),
            num_rows=16,
            num_cols=16,
            cell_size_x=50,
            cell_size_y=50,
    )
    m.solve()

    win.wait_for_close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
