from window import Window, Line, Point

class Cell():
    def __init__(self,
                 win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo = False):
        color = "red"
        if undo:
            color = "gray"

        # unpacking tuple from get_center
        start_x, start_y = self.get_center()
        end_x, end_y = to_cell.get_center()

        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        self._win.draw_line(line, fill_color = color)

    def get_center(self):
        return (self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2