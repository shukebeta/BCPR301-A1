from tigr.tigr_interface import AbstractSourceReader


class SourceReader(AbstractSourceReader):
    """ responsible for providing source text for parsing and drawing
        Initiates the Draw use-case.
        Links to a parser and passes the source text onwards
    """

    def __init__(self, parser, optional_file_name=None):
        super().__init__(parser, optional_file_name)
        try:
            with open(optional_file_name) as file:
                for line in file:
                    line = line.strip()
                    if line != '':
                        self.source.append(line)
        except Exception as e:
            print(e)

    def go(self):
        self.parser.parse(self.source)
