from turtle import Turtle
import time

class TurtleWorker(Turtle):
    def __init__(self, speed=6, pencolor='black', pensize=2):
        super().__init__()
        self.__name__ = 'turtle'
        self.set_pencolor(pencolor)
        self.set_speed(speed)
        self.pensize(int(pensize))

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

    def set_pencolor(self, color):
        self.pencolor(color)

    def set_speed(self, speed):
        speed = int(speed)
        if speed > 10:
            speed = 0
        elif speed <= 0:
            speed = 1
        self.speed(speed)

    def bye(self):
        time.sleep(0.5)

    def set_speed(self, speed):
        pass

