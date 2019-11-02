from abc import ABCMeta, abstractmethod


class AbstractWorker(metaclass=ABCMeta):
    name = ''

    @abstractmethod
    def __init__(self, speed, pencolor, pensize):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setheading(self, direction):
        pass

    @abstractmethod
    def penup(self):
        pass

    @abstractmethod
    def pendown(self):
        pass

    @abstractmethod
    def pensize(self, size):
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
    def speed(self, speed):
        pass

    @abstractmethod
    def pencolor(self, pencolor):
        pass

    @abstractmethod
    def draw_line(self, direction, distance):
        pass

    @property
    @abstractmethod
    def heading(self):
        pass
