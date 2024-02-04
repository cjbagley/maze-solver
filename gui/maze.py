from gui.cell import Cell
from gui.point import Point
from gui.window import Window
import time

class Maze:
    """ Holds all the cells in the maze in a 2d grid, a list of lists """
    def __init__(
            self,
            window: Window,
            starting_point: Point,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
        ) -> None:
        self.__win = window
        self.__start = starting_point
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__cells = []
        self.__create_cells()

    def __create_cells(self) -> None:
        for i in range(1, self.__num_cols + 1):
            col = []
            for j in range(1, self.__num_rows + 1):
                tl = self.__get_top_left(i, j)
                br = self.__get_bottom_right(i, j)
                cell = Cell(self.__win, tl, br)
                cell.draw()
                self.__animate()
                col.append(cell)
            self.__cells.append(col)

    def __get_top_left(self, col: int, row: int) -> Point:
        if col == 1 and row == 1:
            return self.__start
        x = self.__start.x + ((col - 1) * self.__cell_size_x)
        y = self.__start.y + ((row - 1) * self.__cell_size_y)
        return Point(x, y)

    def __get_bottom_right(self, col: int, row: int) -> Point:
        x = self.__start.x + (col * self.__cell_size_x)
        y = self.__start.y + (row * self.__cell_size_y)
        return Point(x, y)

    def __animate(self) -> None:
        self.__win.redraw()
        time.sleep(.05)
