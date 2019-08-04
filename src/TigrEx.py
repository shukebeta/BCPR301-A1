from TIGr import AbstractDrawer, AbstractParser, AbstractSourceReader

"""These implementations should be replaced,
by more flexible, portable and extensible solutions.
"""


class Drawer(AbstractDrawer):
    """ Responsible for printing as text what the drawing commands are"""

    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        print('pen down')

    def pen_up(self):
        print('pen up')

    def go_along(self, along):
        print(f'GOTO X={along}')

    def go_down(self, down):
        print(f'GOTO Y={down}')

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction} degrees')


class Parser(AbstractParser):

    def parse(self, raw_source):
        """hard coded parsing like this is a Bad Thing!
            It is inflexible and has no error checking
        """
        self.source = raw_source
        for line in self.source:
            self.command = line[0]
            try:
                self.data = int(line[2])
            except:
                self.data = 0
            if self.command == 'P':
                self.drawer.select_pen(self.data)
            if self.command == 'D':
                self.drawer.pen_down()
            if self.command == 'G':
                self.drawer.goto(self.data)
            if self.command == 'N':
                self.drawer.draw_line(0, self.data)
            if self.command == 'E':
                self.drawer.draw_line(90, self.data)
            if self.command == 'S':
                self.drawer.draw_line(180, self.data)
            if self.command == 'W':
                self.drawer.draw_line(270, self.data)
            if self.command == 'X':
                self.drawer.go_along(self.data)
            if self.command == 'Y':
                self.drawer.go_down(self.data)
            if self.command == 'U':
                self.drawer.pen_up()


class SourceReader(AbstractSourceReader):
    """ responsible for providing source text for parsing and drawing
        Initiates the Draw use-case.
        Links to a parser and passes the source text onwards
    """

    def go(self):
        self.source.append('P 2 # select pen 2')
        self.source.append('X 5 # go to 5 along')
        self.source.append('Y 15 # go to 15 down')
        self.source.append('D  # pen down')
        self.source.append('W 2    # draw west 2cm')
        self.source.append('N 1    # then north 1')
        self.source.append('E 2    # then east 2')
        self.source.append(' S  12.7 ')
        self.source.append(' U # pen up')
        self.parser.parse(self.source)


if __name__ == '__main__':
    s = SourceReader(Parser(Drawer()))
    s.go()

