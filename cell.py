from window import Window, Line, Point

class Cell():
    def __init__(self, 
                 has_left_wall = True,
                 has_right_wall = True,
                 has_top_wall = True,
                 has_bottom_wall = True,
                 x1=None,
                 x2=None,
                 y1=None,
                 y2=None,
                 Window=None):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = Window
    
    def draw(self):
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        top_right = Point(bottom_right.x, top_left.y)
        bottom_left = Point(top_left.x, bottom_right.y)

        if self.has_left_wall:
            self._win.draw_line(
                Line(top_left, bottom_left)
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(top_right, bottom_right)
            )
        if self.has_top_wall:
            self._win.draw_line(
                Line(top_left, top_right)
            )
        if self.has_bottom_wall:
            self._win.draw_line(
               Line(bottom_left, bottom_right)
            )