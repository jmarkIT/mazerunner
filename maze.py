import random
from time import sleep
from graphics import Window
from cell import Cell

random.seed()


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed: int | float | None = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        else:
            random.seed(0)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for _ in range(self.num_cols):
            col = []
            for _ in range(self.num_rows):
                col.append(Cell(self._win))  # type: ignore
            self._cells.append(col)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        if self._win is None:
            return
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._animate()
        last_col = self.num_cols - 1
        last_row = self.num_rows - 1
        self._cells[last_col][last_row].has_bottom_wall = False
        self._draw_cell(
            last_col,
            last_row,
        )
        self._animate()

    def _break_walls_r(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Check cell above
            if i != 0:
                if self._cells[i - 1][j].visited is False:
                    to_visit.append([i - 1, j])
            # Check cell below
            if i != self.num_cols - 1:
                if self._cells[i + 1][j].visited is False:
                    to_visit.append([i + 1, j])
            # Check cell to left
            if j != 0:
                if self._cells[i][j - 1].visited is False:
                    to_visit.append([i, j - 1])
            # Check cell to right
            if j != self.num_rows - 1:
                if self._cells[i][j + 1].visited is False:
                    to_visit.append([i, j + 1])
            if not to_visit:
                self._draw_cell(i, j)
                return
            to_cell = random.choice(to_visit)
            i2, j2 = to_cell[0], to_cell[1]
            if i2 < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i2][j2].has_right_wall = False
                self._draw_cell(i, j)
                self._animate()
            if i2 > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i2][j2].has_left_wall = False
                self._draw_cell(i, j)
                self._animate()
            if j2 < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i2][j2].has_bottom_wall = False
                self._draw_cell(i, j)
                self._animate()
            if j2 > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i2][j2].has_top_wall = False
                self._draw_cell(i, j)
                self._animate()
            self._break_walls_r(i2, j2)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        # Move Up
        try:
            if (
                j - 1 >= 0
                and current_cell.has_top_wall is False
                and self._cells[i][j - 1].visited is False
            ):
                next_cell = self._cells[i][j - 1]
                self._cells[i][j].draw_move(next_cell)
                r = self._solve_r(i, j - 1)
                if r is True:
                    return True
                self._cells[i][j].draw_move(next_cell, undo=True)
        except IndexError:
            pass
        # Move Down
        try:
            if (
                j + 1 <= self.num_rows
                and current_cell.has_bottom_wall is False
                and self._cells[i][j + 1].visited is False
            ):
                next_cell = self._cells[i][j + 1]
                self._cells[i][j].draw_move(next_cell)
                r = self._solve_r(i, j + 1)
                if r is True:
                    return True
                self._cells[i][j].draw_move(next_cell, undo=True)
        except IndexError:
            pass
        # Move Right
        try:
            if (
                i + 1 <= self.num_cols
                and current_cell.has_right_wall is False
                and self._cells[i + 1][j].visited is False
            ):
                next_cell = self._cells[i + 1][j]
                self._cells[i][j].draw_move(next_cell)
                r = self._solve_r(i + 1, j)
                if r is True:
                    return True
                self._cells[i][j].draw_move(next_cell, undo=True)
        except IndexError:
            pass
        # Move Left
        try:
            if (
                i - 1 >= 0
                and current_cell.has_left_wall is False
                and self._cells[i - 1][j].visited is False
            ):
                next_cell = self._cells[i - 1][j]
                self._cells[i][j].draw_move(next_cell)
                r = self._solve_r(i - 1, j)
                if r is True:
                    return True
                self._cells[i][j].draw_move(next_cell, undo=True)
        except IndexError:
            pass
        return False
