from tigr.tigr_interface import AbstractDrawer

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)
debug = logging.debug


class Drawer(AbstractDrawer):

    def __init__(self, worker):
        self.worker = worker
        super().__init__()

    def select_pen(self, pen_num):
        return self.worker.select_pen(pen_num)

    def pen_down(self):
        return self.worker.pendown()
        debug('pen is down')

    def pen_up(self):
        return self.worker.penup()
        debug('pen is up')

    def go_along(self, along):
        return self.worker.go_along(int(along))
        debug(f'go along X: {along}')

    def go_down(self, down):
        return self.worker.go_down(int(down))
        debug(f'go along Y: {down}')

    def draw_line(self, direction, distance):
        return self.worker.draw_line(int(direction), int(distance))
        debug(f'draw a line with length: {distance}, direction: {direction} degree.' )

    def __getattr__(self, method_name):
        def func(*args, **kwargs):
            return self._call_method(method_name, *args, **kwargs)
        return func

    def _call_method(self, method_name, *args, **kwargs):
        return getattr(self.worker, method_name)(*args, **kwargs)

    def do_draw_command(self, cmd, operand):
        cmd = cmd.upper()
        draw_methods = {
            'D': self.pen_down,
            'U': self.pen_up,
            'G': self.goto,
            'N': self.draw_line,
            'S': self.draw_line,
            'W': self.draw_line,
            'E': self.draw_line,
            'P': self.select_pen,
            'X': self.go_along,
            'Y': self.go_down,
            'L': self.draw_line,
        }
        draw_degrees = {
            'N': 90,
            'S': 270,
            'E': 0,
            'W': 180,
        }

        if cmd in draw_degrees:
            operand.insert(0, draw_degrees[cmd])
        if cmd in draw_methods:
            return draw_methods[cmd](*operand)
        return False

