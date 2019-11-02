from abc import ABC, abstractmethod

""" Tiny Interpreted GRaphic = TIGR
Keep the interfaces defined below in your work.
 """

class AbstractSourceReader(ABC):
    """ responsible for providing source text for parsing and drawing
        Initiates the Draw use-case.
        Links to a parser and passes the source text onwards
    """

    def __init__(self, parser, optional_file_name=None):
        self.parser = parser
        self.file_name = optional_file_name
        self.source = []

    @abstractmethod
    def go(self):
        pass
