import tkinter as tk
import math
import time


class TkinterWorker(tk.Tk):
    name = 'tkinter'
    def __init__(self, speed=6, pencolor='black', pensize=2):
        super().__init__()
        self.title("Tkinter drawer")
        self.geometry("800x600")
        self._pencolor = str(pencolor)
        self._pensize = int(pensize)
        self.speed(int(speed))

        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack(side=tk.TOP, fill=tk.X)
        self.home_pos = (400, 300)
        self.pos = {
            'x': 400,
            'y': 300
        }
        self._pendown = True
        self._heading = 90

    def setheading(self, direction):
        self._heading = direction

    def penup(self):
        self._pendown = False
        self.debug()

    def pendown(self):
        self._pendown = True
        self.debug()

    def pensize(self, size):
        self._pensize = int(size)

    def go_down(self, length):
        if length > 0:
            heading = 0
        else:
            heading = 180
        self.setheading(heading)
        self.forward(abs(length))
        self.debug()

    def forward(self, length):
        x, y = self._calc_target_pos(self._heading, length)
        if self._pendown:
            self._draw_line(x, y)
        else:
            self.goto(x, y)

        self.update()
        self.debug()

    def goto(self, x, y):
        self.pos['x'] = x
        self.pos['y'] = y

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

    def speed(self, speed):
        wait = 1 / speed
        if speed <= 0: wait = 1
        self.wait = wait

    def pencolor(self, pencolor):
        self._pencolor = pencolor

    def debug(self):
        # print(self.pos)
        pass

    def update(self):
        super().update()
        time.sleep(self.wait)

    def draw_line(self, direction, distance):
        # to get same behaviour as turtle
        direction += 90
        self._heading = direction
        x, y = self._calc_target_pos(direction, distance)

        if not self._pendown:
            self.pendown()
            self._draw_line(x, y)
            self.penup()
        else:
            self._draw_line(x, y)


    def _draw_line(self, x, y):
        self.canvas.create_line(self.pos['x'], self.pos['y'], x, y, fill=self._pencolor, width=self._pensize)
        self.goto(x, y)
        self.update()
        self.debug()

    def _calc_target_pos(self, direction, length):
        return (self.pos['x'] + math.sin(math.radians(direction)) * length,
                self.pos['y'] + math.cos(math.radians(direction)) * length)
    @property
    def heading(self):
        return self._heading - 90

if __name__ == '__main__':
    root = TkinterWorker()
    root.mainloop()
