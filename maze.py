from cell import Cell
import time

class Maze():   
    def __init__(
            self,
            x1, 
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = []

        # create all cells
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)

        # draw all cells
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        pos_x = self.x1 + (i * self.cell_size_x)
        pos_y = self.y1 + (j * self.cell_size_y)

        self._cells[i][j].draw(pos_x, pos_y, 
                  (pos_x + self.cell_size_x), 
                  (pos_y + self.cell_size_y))
        
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

