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
        self._win = window
        self._start = starting_point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if seed > 0:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        for i in range(1, self._num_cols + 1):
            col = []
            for j in range(1, self._num_rows + 1):
                tl = self._get_top_left(i, j)
                br = self._get_bottom_right(i, j)
                cell = Cell(self._win, tl, br)
                cell.draw()
                self._animate()
                col.append(cell)
            self._cells.append(col)

    def _get_top_left(self, col: int, row: int) -> Point:
        if col == 1 and row == 1:
            return self._start
        x = self._start.x + ((col - 1) * self._cell_size_x)
        y = self._start.y + ((row - 1) * self._cell_size_y)
        return Point(x, y)

    def _get_bottom_right(self, col: int, row: int) -> Point:
        x = self._start.x + (col * self._cell_size_x)
        y = self._start.y + (row * self._cell_size_y)
        return Point(x, y)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()

        exit_cell = self._cells[self._num_cols-1][self._num_rows-1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw()

    def _animate(self) -> None:
        self._win.redraw()
        time.sleep(.01)
    
    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            # Adjacent top cell
            if j-1 >= 0 and self._cells[i][j-1].visited == False:
                to_visit.append(("top", i, j-1))
            # Adjacent right cell
            if i+1 < self._num_cols and self._cells[i+1][j].visited == False:
                to_visit.append(("right", i+1, j))
            # Adjacent bottom cell
            if j+1 < self._num_rows and self._cells[i][j+1].visited == False:
                to_visit.append(("bottom", i, j+1))
            # Adjacent left cell
            if i-1 >= 0 and self._cells[i-1][j].visited == False:
                to_visit.append(("left", i-1, j))
            if len(to_visit) == 0:
                return
            direction = random.choice(to_visit)
            chosen = self._cells[direction[1]][direction[2]]

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
            self._break_walls_r(direction[1], direction[2])

    def _reset_cells_visited(self):
        for x in range(0, self._num_cols):
            for y in range(0, self._num_rows):
                self._cells[x][y].visited = False