from tigr.tigr_interface import AbstractParser
from abc import abstractmethod


class StrategyParser(AbstractParser):

    def __init__(self, drawer):
        super().__init__(drawer)
        self.draw_methods = {
            'D': self.drawer.pen_down,
            'U': self.drawer.pen_up,
            'G': self.drawer.goto,
            'N': self.drawer.draw_line,
            'S': self.drawer.draw_line,
            'W': self.drawer.draw_line,
            'E': self.drawer.draw_line,
            'P': self.drawer.select_pen,
            'X': self.drawer.go_along,
            'Y': self.drawer.go_down,
            'L': self.drawer.draw_line,
        }
        self.draw_degrees = {
            'N': 90,
            'S': 270,
            'E': 0,
            'W': 180,
        }

    @abstractmethod
    def parse(self, file):
        raise NotImplementedError()

    def do(self, command):
        if command['cmd'] in self.draw_degrees:
            command['operand'].insert(0, self.draw_degrees[command['cmd']])
        self.draw_methods[command['cmd']](*command['operand'])
