from tkinter import Tk, BOTH, Canvas
from window import Window, Line, Point

def main():
    win = Window(800, 600)
    line_test = Line(Point(50,50), Point(400,400))
    win.draw_line(line_test, "black")
    win.wait_for_close()

main()