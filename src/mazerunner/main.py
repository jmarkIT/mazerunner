from maze import Maze
from graphics import Window
from random import random


def main():
    win = Window(800, 600)

    seed = random()
    m = Maze(10, 10, 10, 15, 50, 50, win, seed)

    m.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()