from abc import ABCMeta, abstractmethod


class AbstractWorker(metaclass=ABCMeta):
    name = ''
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

    @abstractmethod
    def __init__(self, speed, pencolor, pensize):
        pass

    def select_pen(self, pen):
        pen = int(pen)
        if pen < 1 or pen > 9:
            print(f'invalid pen: {pen}, it should be a integer between 1 and 9')
            return False
        self.pensize(self.pen_list[pen - 1]['pensize'])
        self.pencolor(self.pen_list[pen - 1]['pencolor'])

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setheading(self, direction):
        pass

    @abstractmethod
    def pen_up(self):
        pass

    @abstractmethod
    def pen_down(self):
        pass

    @abstractmethod
    def pensize(self, size=None):
        pass

    @abstractmethod
    def go_down(self, length):
        pass

    @abstractmethod
    def forward(self, length):
        pass

    @abstractmethod
    def goto(self, x, y):
        pass

    @abstractmethod
    def go_along(self, along):
        pass

    @abstractmethod
    def bye(self):
        pass

    @abstractmethod
    def speed(self, speed=None):
        pass

    @abstractmethod
    def pencolor(self, pencolor=None):
        pass

    @abstractmethod
    def draw_line(self, direction, distance):
        pass

    @property
    @abstractmethod
    def heading(self):
        pass
