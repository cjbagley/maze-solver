from tkinter import Tk, BOTH, Canvas
from gui.line import Line
from gui.point import Point

class Window:
    """ Root window component """
    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, height=self._height, width=self._width, background="white")
        self._canvas.pack(fill=BOTH, expand=1)
        self._isRunning = False

    def redraw(self) -> None:
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        self._isRunning = True
        while self._isRunning:
            self.redraw()

    def close(self) -> None:
        self._isRunning = False

    def draw_line(self, line: Line, fill_color="black") -> None:
        line.draw(self._canvas, fill_color)
