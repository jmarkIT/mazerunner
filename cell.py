from graphics import Window, Point, Line


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
