from components.point import Point
from tkinter import Canvas

class Line:
    """ Handles drawing a line from point a to point b """
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self.__point_a = point_a
        self.__point_b = point_b
    
    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
         self.__point_a.x, self.__point_a.y, self.__point_b.x, self.__point_b.y, fill=fill_color, width=2
        )
        canvas.pack(fill='both', expand=1)
