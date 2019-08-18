
from tigr.tigr_interface import AbstractDrawer
class Drawer(AbstractDrawer):
    def __init__(self, worker):
        self.worker = worker
        super(Drawer, self).__init__()

    def select_pen(self, pen):
        pass

    def pen_down(self):
        self.worker.pendown()
        print('pen is down')

    def pen_up(self):
        self.worker.penup()
        print('pen is up')

    def pen_color(self, color):
        self.worker.set_pencolor(color)

    def go_along(self, along):
        self.worker.go_along(int(along))
        print(f'go along X: {along}')

    def go_down(self, down):
        self.worker.go_down(int(down))
        print(f'go along Y: {down}')

    def draw_line(self, direction, distance):
        self.worker.draw_line(int(direction), int(distance))
        print(f'draw a line with length: {distance}, direction: {direction} degree.' )

    def bye(self):
        self.worker.bye()

    @property
    def pos(self):
        return self.worker.pos()

