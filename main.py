from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(100, 100, 150, 150)

    c.draw_move(c1)

    win.wait_for_close()

main()