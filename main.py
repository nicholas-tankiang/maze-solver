from tkinter import Tk, BOTH, Canvas
from window import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    #line_test = Line(Point(50,50), Point(400,400))
    #win.draw_line(line_test, "black")
    cell_test = Cell(True, False, False, False, 50, 70, 50, 70, win)
    cell_test.draw()
    win.wait_for_close()

main()