
from tigr.tigr_interface import AbstractDrawer
class Drawer(AbstractDrawer):
    def __init__(self, worker):
        self.worker = worker

    def select_pen(self, pen):
        pass

    def pen_down(self):
        self.worker.pendown()

    def pen_up(self):
        self.worker.penup()

    def go_along(self, along):
        x, y = self.pos
        self.worker.goto(x+along, y)

    def go_down(self, down):
        x, y = self.pos
        self.worker.goto(x, y+down)

    def draw_line(self, direction, distance):
        self.pen_down()
        self.worker.setheading(direction)
        self.worker.forward(distance)

    def bye(self):
        self.worker.bye()

    @property
    def pos(self):
        return self.worker.pos()


