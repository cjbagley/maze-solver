from gui.point import Point
from tkinter import Canvas

class Line:
    """ Handles drawing a line from point a to point b """
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self._point_a = point_a
        self._point_b = point_b
    
    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
         self._point_a.x, self._point_a.y, self._point_b.x, self._point_b.y, fill=fill_color, width=2
        )
        canvas.pack(fill='both', expand=1)
