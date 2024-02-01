#!/usr/bin/env python
import sys
from components.window import Window
from components.line import Line
from components.point import Point

def main() -> int:
    """Maze solver"""
    win = Window(800, 800)
    line_a = Line(Point(0, 200), Point(200, 200))
    win.draw_line(line_a, "black")
    line_b = Line(Point(650, 507), Point(522, 2))
    win.draw_line(line_b, "purple")
    win.wait_for_close()
    return 0

if __name__ == '__main__':
    sys.exit(main())