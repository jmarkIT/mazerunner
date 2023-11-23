from dataclasses import dataclass
from tkinter import Tk, Canvas


@dataclass
class Point:
    """Dataclass to represent a single point in x-y coordinates"""

    x: int
    y: int


class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, color):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=color,
            width=2,
        )
        canvas.pack()


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running is True:
            self.redraw()

    def close(self):
        """Closes the window."""
        self.is_running = False

    def draw_line(self, line: Line, color: str):
        line.draw(self.canvas, color)
