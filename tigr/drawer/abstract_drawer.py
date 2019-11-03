from abc import ABC, abstractmethod

""" Tiny Interpreted GRaphic = TIGR
Keep the interfaces defined below in your work.
 """


class AbstractDrawer(ABC):
    """ Responsible for defining an interface for drawing """

    @abstractmethod
    def select_pen(self, pen_num):
        pass

    @abstractmethod
    def pen_down(self):
        pass

    @abstractmethod
    def pen_up(self):
        pass

    @abstractmethod
    def go_along(self, along):
        pass

    @abstractmethod
    def go_down(self, down):
        pass

    @abstractmethod
    def draw_line(self, direction, distance):
        pass
