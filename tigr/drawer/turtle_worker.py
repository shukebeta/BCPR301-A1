from tigr.drawer.abstract_worker import AbstractWorker
from turtle import Turtle
import time


class TurtleWorker(AbstractWorker):
    name = 'turtle'

    def __init__(self, speed=6, pencolor='black', pensize=2):
        super().__init__(speed, pencolor, pensize)
        self.turtle = Turtle()
        self.pencolor(pencolor)
        self.speed(speed)
        self.pensize(int(pensize))
        self.goto(400, 300)

    def forward(self, distance):
        return self.turtle.forward(distance)

    def setheading(self, to_angle):
        return self.turtle.setheading(to_angle)

    def pencolor(self, *args):
        return self.turtle.pencolor(*args)

    def pen_down(self):
        return self.turtle.pendown()

    def pensize(self, *args):
        return self.turtle.pensize(*args)

    def pen_up(self):
        return self.turtle.penup()

    def reset(self):
        return self.turtle.reset()

    def go_down(self, length):
        if length > 0:
            heading = 270
        else:
            heading = 90
        self.setheading(heading)
        self.forward(abs(length))

    def go_along(self, along):
        if along > 0:
            heading = 0
        else:
            heading = 180
        self.setheading(heading)
        self.forward(abs(along))

    def draw_line(self, direction, distance):
        self.pen_down()
        self.setheading(direction)
        self.forward(distance)

    def goto(self, x, y):
        x, y = self._convert_x_y(x, y)
        if self.turtle.pen()['pendown']:
            self.pen_up()
            self.turtle.goto(x, y)
            self.pen_down()
        else:
            self.turtle.goto(x, y)

    def _convert_x_y(self, x, y):
        x -= 400
        if y > 300:
            y -= 2 * y - 300
        else:
            y = 300 - y
        return (x, y)

    def speed(self, speed=None):
        if speed is None:
            return self.turtle.speed()

        speed = int(speed)
        if speed > 10:
            speed = 0
        elif speed <= 0:
            speed = 1
        self.turtle.speed(speed)

    def bye(self):
        time.sleep(0.5)

    def pos(self):
        return tuple([int(i) for i in self.turtle.pos()])

    def __getattr__(self, method_name):
        def func(*args, **kwargs):
            return self._call_method(method_name, *args, **kwargs)
        return func

    def _call_method(self, method_name, *args, **kwargs):
        return getattr(self.turtle, method_name)(*args, **kwargs)

    @property
    def heading(self):
        return self.turtle.heading

