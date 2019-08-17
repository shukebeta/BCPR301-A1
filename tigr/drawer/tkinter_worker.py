import tkinter as tk
import math
import time

class TkinterWorker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter drawer")
        self.geometry("800x600")
        self.pen_color = 'black'

        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack(side=tk.TOP, fill=tk.X)
        self.home_pos = (400, 300)
        self.current_pos = {
            'x': 400,
            'y': 300
        }
        self._pendown = True
        self.heading = 90
        self.__name__ = 'tkinter'
        self.wait = 0.5 # seconds

    def setheading(self, direction):
        self.heading = direction

    def penup(self):
        self._pendown = False
        self.debug()

    def pendown(self):
        self._pendown = True
        self.debug()

    def go_down(self, length):
        if length > 0:
            heading = 0
        else:
            heading = 180
        self.setheading(heading)
        self.forward(abs(length))
        self.debug()

    def forward(self, length):
        x, y = self._calc_target_pos(self.heading, length)
        if self._pendown:
            self._draw_line(x, y)
        else:
            self.goto(x, y)

        self.update()
        self.debug()

    def goto(self, x, y):
        self.current_pos['x'] = x
        self.current_pos['y'] = y

        self.update()
        self.debug()

    def go_along(self, along):
        if along > 0:
            heading = 90
        else:
            heading = 270
        self.setheading(heading)
        self.forward(abs(along))

    def bye(self):
        self.quit()
        self.update()
        time.sleep(0.5)

    def set_speed(self, speed):
        wait = 1 / speed
        if speed <= 0: wait = 1
        self.wait = wait

    def set_pen_color(self, pen_color):
        self.pen_color = pen_color

    @property
    def pos(self):
        return self.current_pos

    def debug(self):
        # print(self.pos)
        pass

    def update(self):
        super().update()
        time.sleep(self.wait)


    def _draw_line(self, x, y):
        self.canvas.create_line(self.current_pos['x'], self.current_pos['y'], x, y, fill=self.pen_color)
        self.goto(x, y)
        self.update()
        self.debug()

    def _calc_target_pos(self, direction, length):
        return (self.current_pos['x'] + math.sin(math.radians(direction)) * length,
                self.current_pos['y'] + math.cos(math.radians(direction)) * length)

if __name__ == '__main__':
    root = TkinterWorker()
    root.mainloop()
