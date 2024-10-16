from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("A Window")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        canvas_widget = Canvas()
        canvas_widget.pack()
        self.is_running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running == True:
            self.redraw()
    
    def close(self):
        self.is_running = False
