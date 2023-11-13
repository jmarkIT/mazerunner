from cell import Cell
from graphics import Window


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
