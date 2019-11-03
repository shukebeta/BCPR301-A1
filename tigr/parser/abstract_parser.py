from abc import ABC, abstractmethod

""" Tiny Interpreted GRaphic = TIGR
Keep the interfaces defined below in your work.
 """


class AbstractParser(ABC):
    def __init__(self, drawer):
        self.drawer = drawer
        self.source = []
        self.command = ''
        self.data = 0

    @abstractmethod
    def parse(self, raw_source):
        pass
