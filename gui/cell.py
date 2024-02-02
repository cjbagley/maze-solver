from gui.window import Window
from gui.line import Line
from gui.point import Point

class Cell:
    """ Individual maze cell from the grid """
    def __init__(self, window: Window, top_left_point: Point, bottom_right_point: Point ) -> None:
        self.__window = window
        self.__tl_x = top_left_point.x
        self.__tl_y = top_left_point.y
        self.__br_x = bottom_right_point.x
        self.__br_y = bottom_right_point.y
        # walls can be removed via public change
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    
    def draw(self) -> None:
        if self.has_right_wall:
            wall = Line(Point(self.__br_x, self.__tl_y), Point(self.__br_x, self.__br_y))
            self.__window.draw_line(wall)
        if self.has_left_wall:
            wall = Line(Point(self.__tl_x, self.__tl_y), Point(self.__tl_x, self.__br_y))
            self.__window.draw_line(wall)
        if self.has_top_wall:
            wall = Line(Point(self.__tl_x, self.__tl_y), Point(self.__br_x, self.__tl_y))
            self.__window.draw_line(wall)
        if self.has_bottom_wall:
            wall = Line(Point(self.__tl_x, self.__br_y), Point(self.__br_x, self.__br_y))
            self.__window.draw_line(wall)
        print(self)
    
    def draw_move(self, to_cell: 'Cell', undo:bool=False) -> None:
        line_color = "gray"
        if undo:
            line_color = "red"
        line = Line(self.get_middle(), to_cell.get_middle())
        self.__window.draw_line(line, line_color)

    def get_middle(self) -> Point:
        x = (self.__br_x + self.__tl_x) / 2
        y = (self.__br_y + self.__tl_y) / 2
        return Point(x, y)

    def __str__(self) -> str:
        str = ""
        str += f"Top left: {self.__tl_x}, {self.__tl_y}\n"
        str += f"Bottom right: {self.__br_x}, {self.__br_y}\n"
        mid = self.get_middle()
        str += f"Mid: {mid.x}, {mid.y}\n"
        return str
