#!/usr/bin/env python
import sys
from gui.window import Window
from gui.line import Line
from gui.point import Point
from gui.cell import Cell 

def main() -> int:
    """Maze solver"""
    win = Window(800, 800)
    cell = Cell(win, Point(10, 10), Point(790, 790))
    cell.draw()
    win.wait_for_close()
    return 0

if __name__ == '__main__':
    sys.exit(main())