from gui.cell import Cell
from gui.point import Point
from gui.window import Window
import time
import random

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
            seed: int=0,
        ) -> None:
        self.__win = window
        self.__start = starting_point
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        if seed > 0:
            random.seed(seed)
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)

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

    def __break_entrance_and_exit(self):
        entrance_cell = self.__cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()

        exit_cell = self.__cells[self.__num_cols-1][self.__num_rows-1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw()

    def __animate(self) -> None:
        self.__win.redraw()
        time.sleep(.01)
    
    def __break_walls_r(self, i, j):
        current = self.__cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            # Adjacent top cell
            if j-1 >= 0 and self.__cells[i][j-1].visited == False:
                to_visit.append(("top", i, j-1))
            # Adjacent right cell
            if i+1 < self.__num_rows and self.__cells[i+1][j].visited == False:
                to_visit.append(("right", i+1, j))
            # Adjacent bottom cell
            if j+1 < self.__num_cols and self.__cells[i][j+1].visited == False:
                to_visit.append(("bottom", i, j+1))
            # Adjacent left cell
            if i-1 >= 0 and self.__cells[i-1][j].visited == False:
                to_visit.append(("left", i-1, j))
            if len(to_visit) == 0:
                return
            direction = random.choice(to_visit)
            chosen = self.__cells[direction[1]][direction[2]]

            if direction[0] == 'top':
                chosen.has_bottom_wall = False 
                current.has_top_wall = False
            elif direction[0] == 'right':
                chosen.has_left_wall = False 
                current.has_right_wall = False 
            elif direction[0] == 'bottom':
                chosen.has_top_wall = False 
                current.has_bottom_wall = False
            else:
                chosen.has_right_wall = False 
                current.has_left_wall = False 
            current.draw()
            chosen.draw()
            self.__break_walls_r(direction[1], direction[2])

