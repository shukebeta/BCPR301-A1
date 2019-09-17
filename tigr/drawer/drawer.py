from tigr.tigr_interface import AbstractDrawer

import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)
debug = logging.debug


class Drawer(AbstractDrawer):
    pen_list =[
        {
            'pencolor': 'black',
            'pensize': 1
        },
        {
            'pencolor': 'black',
            'pensize': 2
        },
        {
            'pencolor': 'black',
            'pensize': 3
        },
        {
            'pencolor': 'red',
            'pensize': 1
        },
        {
            'pencolor': 'red',
            'pensize': 2
        },
        {
            'pencolor': 'red',
            'pensize': 3
        },
        {
            'pencolor': 'blue',
            'pensize': 1
        },
        {
            'pencolor': 'blue',
            'pensize': 2
        },
        {
            'pencolor': 'blue',
            'pensize': 3
        },
    ]

    def __init__(self, worker):
        self.worker = worker
        super().__init__()

    def select_pen(self, pen):
        """pen should be a integer from 1 to 9, every pen has a pencolor and pensize attribute
        """
        pen = int(pen)
        if pen < 1 or pen > 9:
            debug(f'invalid pen: {pen}, should be a integer between 1 and 9')
            return False
        self.pensize(self.pen_list[pen - 1]['pensize'])
        self.pencolor(self.pen_list[pen - 1]['pencolor'])

    def pen_down(self):
        self.worker.pendown()
        debug('pen is down')

    def pen_up(self):
        self.worker.penup()
        debug('pen is up')

    def go_along(self, along):
        self.worker.go_along(int(along))
        debug(f'go along X: {along}')

    def go_down(self, down):
        self.worker.go_down(int(down))
        debug(f'go along Y: {down}')

    def draw_line(self, direction, distance):
        self.worker.draw_line(int(direction), int(distance))
        debug(f'draw a line with length: {distance}, direction: {direction} degree.' )

    def __getattr__(self, method_name):
        def func(*args, **kwargs):
            self._call_method(method_name, *args, **kwargs)
        return func

    def _call_method(self, method_name, *args, **kwargs):
        getattr(self.worker, method_name)(*args, **kwargs)


