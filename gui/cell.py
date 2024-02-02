from gui.window import Window
from gui.line import Line
from gui.point import Point
from tkinter import Canvas

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
            self.__window.draw_line(wall, "blue")
        if self.has_left_wall:
            wall = Line(Point(self.__tl_x, self.__tl_y), Point(self.__tl_x, self.__br_y))
            self.__window.draw_line(wall, "purple")
        if self.has_top_wall:
            wall = Line(Point(self.__tl_x, self.__tl_y), Point(self.__br_x, self.__tl_y))
            self.__window.draw_line(wall, "green")
        if self.has_bottom_wall:
            wall = Line(Point(self.__tl_x, self.__br_y), Point(self.__br_x, self.__br_y))
            self.__window.draw_line(wall, "red")