from cell import Cell
from graphics import Window


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)
    cell1.has_right_wall = False
    cell2.has_left_wall, cell2.has_bottom_wall = False, False
    cell3.has_top_wall = False
    cell1.draw(200, 200, 400, 400)
    cell2.draw(400, 200, 600, 400)
    cell3.draw(400, 400, 600, 600)
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    win.wait_for_close()


if __name__ == "__main__":
    main()
