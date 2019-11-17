import tkinter as tk
import math
import time


class TkinterWorker(tk.Tk):
    name = 'tkinter'

    def __init__(self, speed=6, pencolor='black', pensize=2):
        super().__init__()
        self.init_config = {
            'speed': speed,
            'pencolor': pencolor,
            'pensize': pensize
        }
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
        self.setheading(0)
        self.draw_history = []
        self._heading = 90
        self._wait = 0

    def reset(self):
        for item in self.draw_history:
            self.canvas.after(0, self.canvas.delete, item)
        self.draw_history = []
        self._pencolor = self.init_config['pencolor']
        self._pensize = int(self.init_config['pensize'])
        self.speed(int(self.init_config['speed']))
        self.goto(*self.home_pos)
        self.update()

    def setheading(self, direction):
        self._heading = direction + 90

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
            self._heading = 0
        else:
            self._heading = 180
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
            self._heading = 90
        else:
            self._heading = 270
        self.forward(abs(along))

    def bye(self):
        time.sleep(0.5)

    def speed(self, speed):
        wait = 1 / speed
        if speed <= 0:
            wait = 1
        self._wait = wait

    def pencolor(self, pencolor):
        self._pencolor = pencolor

    def debug(self):
        # print(self.pos)
        pass

    def update(self):
        super().update()
        time.sleep(self._wait)

    def draw_line(self, direction, distance):
        # to get same behaviour as turtle
        self._heading = direction + 90
        x, y = self._calc_target_pos(self._heading, distance)

        if not self._pendown:
            self.pendown()
            self._draw_line(x, y)
            self.penup()
        else:
            self._draw_line(x, y)

    def _draw_line(self, x, y):
        item = self.canvas.create_line(self.pos['x'], self.pos['y'], x, y, fill=self._pencolor, width=self._pensize)
        self.draw_history.append(item)
        self.goto(x, y)
        self.update()
        self.debug()

    def _calc_target_pos(self, direction, length):
        return (self.pos['x'] + math.sin(math.radians(direction)) * length,
                self.pos['y'] + math.cos(math.radians(direction)) * length)

    @property
    def heading(self):
        return self._heading - 90
