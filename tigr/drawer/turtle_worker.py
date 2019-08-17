from turtle import Turtle
import time

class TurtleWorker(Turtle):
    def __init__(self):
        super().__init__()
        self.__name__ = 'turtle'

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

    def set_pen_color(self, color):
        self.pencolor(color)

    def bye(self):
        time.sleep(0.5)

    def set_speed(self, speed):
        pass
