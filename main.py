from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    cell_test = Cell(win)
    cell_test.draw(70, 70, 50, 50)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    win.wait_for_close()

main()