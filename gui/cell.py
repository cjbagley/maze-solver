from gui.window import Window
from gui.line import Line
from gui.point import Point

class Cell:
    """ Individual maze cell from the grid """
    def __init__(self, window: Window, top_left_point: Point, bottom_right_point: Point ) -> None:
        self._window = window
        self._tl_x = top_left_point.x
        self._tl_y = top_left_point.y
        self._br_x = bottom_right_point.x
        self._br_y = bottom_right_point.y
        # walls can be removed via public change
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False 

    def draw(self) -> None:
        right_wall = Line(Point(self._br_x, self._tl_y), Point(self._br_x, self._br_y))
        self._draw_wall_line(right_wall, self.has_right_wall)

        left_wall = Line(Point(self._tl_x, self._tl_y), Point(self._tl_x, self._br_y))
        self._draw_wall_line(left_wall, self.has_left_wall)

        top_wall = Line(Point(self._tl_x, self._tl_y), Point(self._br_x, self._tl_y))
        self._draw_wall_line(top_wall, self.has_top_wall)

        bottom_wall = Line(Point(self._tl_x, self._br_y), Point(self._br_x, self._br_y))
        self._draw_wall_line(bottom_wall, self.has_bottom_wall)

    def _draw_wall_line(self, wall: Line, visible:bool=True) -> None:
        if visible:
            self._window.draw_line(wall)
        else:
            self._window.draw_line(wall, "white")

    def draw_move(self, to_cell: 'Cell', undo:bool=False) -> None:
        line_color = "red"
        if undo:
            line_color = "grey"
        line = Line(self.get_middle(), to_cell.get_middle())
        self._window.draw_line(line, line_color)

    def get_middle(self) -> Point:
        x = (self._br_x + self._tl_x) / 2
        y = (self._br_y + self._tl_y) / 2
        return Point(x, y)

    def __str__(self) -> str:
        str = ""
        str += f"Top left: {self._tl_x}, {self._tl_y}\n"
        str += f"Bottom right: {self._br_x}, {self._br_y}\n"
        mid = self.get_middle()
        str += f"Mid: {mid.x}, {mid.y}\n"
        return str
