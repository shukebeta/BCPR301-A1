from tigr.tigr_interface import AbstractParser
class RegexParser(AbstractParser):
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
        }
        self.draw_degrees = {
            'N': 90,
            'S': 270,
            'E': 0,
            'W': 180,
        }

    def parse(self, file):
        import re
        pattern = r'^([DdUuPpNnEeSsWwXxYyGg])\s*(-?[\s\d]+)?'
        p = re.compile(pattern)

        class _Parse():
            def __init__(self, line):
                line = line.strip()
                match = p.match(line)
                # print(line, match)
                self.error_message = ''
                self.command = {
                    'line': line,
                    'operand': []
                }
                if match:
                    cmd, data = match.groups()
                    cmd = cmd.upper()
                    self.command['cmd'] = cmd
                    if data is not None and (cmd == 'U' or cmd == 'D'):
                        self.error_message = f'invalid command: "{line}". {cmd} need not any number but got number(s)'
                    if data is None:
                        if (cmd != 'U' and cmd != 'D'):
                            self.error_message = f'invalid command: "{line}". {cmd} need number(s) but get none'
                    else:
                        print(re.split(r'\s+', data.strip()))
                        operand = [int(i) for i in re.split(r'\s+', data.strip())]
                        count = len(operand)
                        self.command['operand'] = operand
                        if cmd == 'G':
                            if count != 2:
                                self.error_message = f'invalid command: "{line}". {cmd} need 2 numbers but get {count} number(s)'
                                self.command = None
                        else:
                            if count != 1:
                                self.error_message = f'invalid command: "{line}". {cmd} need 1 number but get {count} number(s)'
                                self.command = None
                else:
                    self.error_message = f'invalid command: "{line}". unrecognized command.'

        for line in file:
            cmd = _Parse(line)
            if cmd.error_message == '':
                self.do(cmd.command)
            else:
                print(cmd.error_message)

        import time
        time.sleep(0.5)
        import tigr.shell.cmd as cmd
        cmd.Shell(self.drawer).cmdloop()

    def do(self, command):
        if command['cmd'] in self.draw_degrees:
            command['operand'].insert(0, self.draw_degrees[command['cmd']])
        print(command['operand'])
        self.draw_methods[command['cmd']](*command['operand'])

if __name__ == '__main__':
    from tigr.drawer.drawer import Drawer
    from tigr.drawer.turtle_worker import TurtleWorker as Worker
    parser = RegexParser(Drawer(Worker()))
    parser.parse(open('../test/instructions1.txt'))