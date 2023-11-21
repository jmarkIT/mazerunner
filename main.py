from maze import Maze
from graphics import Window


def main():
    win = Window(800, 600)

    m = Maze(10, 10, 5, 5, 100, 100, win)

    m.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
