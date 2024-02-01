#!/usr/bin/env python
import sys
from components.window import Window

def main() -> int:
    """Maze solver"""
    win = Window(800, 800)
    win.wait_for_close()
    return 0

if __name__ == '__main__':
    sys.exit(main())