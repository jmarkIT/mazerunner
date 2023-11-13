from tkinter import Tk, BOTH, Canvas
from dataclasses import dataclass


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
        self.canvas = Canvas(self.__root, width=width, height=height)
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


class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "red")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "red")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "red")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "red")

    def draw_move(self, to_cell, undo=False):
        pass


def main():
    win = Window(800, 600)
    cell = Cell(200, 200, 400, 400, win)
    cell.has_bottom_wall = False
    cell.has_left_wall = False
    cell.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
