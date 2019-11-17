from turtle import Turtle
import time


class TurtleWorker(Turtle):
    name = 'turtle'
    def __init__(self, speed=6, pencolor='black', pensize=2):
        super().__init__()
        self.__name__ = 'turtle'
        self.pencolor(pencolor)
        self.speed(speed)
        self.pensize(int(pensize))
        self.goto(400, 300)

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
        self.pendown()
        self.setheading(direction)
        self.forward(distance)

    def goto(self, x, y):
        x -= 400
        if y > 300:
            y -= 2 * y - 300
        else:
            y = 300 - y

        if self.pen()['pendown']:
            self.penup()
            super().goto(x, y)
            self.pendown()
        else:
            super().goto(x, y)

    def speed(self, speed):
        speed = int(speed)
        if speed > 10:
            speed = 0
        elif speed <= 0:
            speed = 1
        super().speed(speed)

    def reset(self):
        super().reset()
        self.goto(400, 300)

    def bye(self):
        time.sleep(0.5)

