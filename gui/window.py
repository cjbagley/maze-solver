from tkinter import Tk, BOTH, Canvas
from gui.line import Line
from gui.point import Point

class Window:
    """ Root window component """
    def __init__(self, height, width) -> None:
        self.__height = height
        self.__width = width
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, height=self.__height, width=self.__width, background="black")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isRunning = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()

    def close(self) -> None:
        self.__isRunning = False

    def draw_line(self, line: Line, fill_color="black") -> None:
        line.draw(self.__canvas, fill_color)
