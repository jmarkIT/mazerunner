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
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

    def get_center(self) -> Point:
        x = (self._x1 + self._x2) // 2
        y = (self._y1 + self._y2) // 2
        return Point(x, y)

    def draw_move(self, to_cell: "Cell", undo=False):
        point_1 = self.get_center()
        point_2 = to_cell.get_center()
        line = Line(point_1, point_2)
        if undo is False:
            line_color = "red"
        else:
            line_color = "gray"
        self._win.draw_line(line, line_color)


def main():
    win = Window(800, 600)
    cell1 = Cell(200, 200, 400, 400, win)
    cell2 = Cell(400, 200, 600, 400, win)
    cell3 = Cell(400, 400, 600, 600, win)
    cell1.has_right_wall = False
    cell2.has_left_wall, cell2.has_bottom_wall = False, False
    cell3.has_top_wall = False
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    win.wait_for_close()


if __name__ == "__main__":
    main()
