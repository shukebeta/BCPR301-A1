from tigr.tigr_interface import AbstractParser
from abc import abstractmethod
import re


class StrategyParser(AbstractParser):
    pattern = r'^([DUPNESWXYGL])\s*(-?[\s\d]+)?(?:#.*)?$'
    p = re.compile(pattern, re.IGNORECASE)

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

    def parseline(self, line):
        line = line.strip()
        match = self.p.match(line)
        error_message = ''
        command = {
            'line': line,
            'operand': []
        }
        if match:
            cmd, data = match.groups()
            cmd = cmd.upper()
            command['cmd'] = cmd
            if data is not None and (cmd == 'U' or cmd == 'D'):
                error_message = f'invalid command: "{line}". {cmd} need not any number but got number(s)'
            if data is None:
                if cmd != 'U' and cmd != 'D':
                    error_message = f'invalid command: "{line}". {cmd} need number(s) but get none'
            else:
                print(re.split(r'\s+', data.strip()))
                operand = [int(i) for i in re.split(r'\s+', data.strip())]
                count = len(operand)
                command['operand'] = operand
                if cmd == 'G' or cmd == 'L':
                    if count != 2:
                        error_message = f'invalid command: "{line}". {cmd} need 2 numbers but get {count} number(s)'
                        command = None
                else:
                    if count != 1:
                        error_message = f'invalid command: "{line}". {cmd} need 1 number but get {count} number(s)'
                        command = None
        else:
            if line[0] == '#':
                error_message = f'skip comment line: {line}'
            else:
                error_message = f'invalid command: "{line}". unrecognized command.'
        return {
            'error_message': error_message,
            'command': command,
        }

    @abstractmethod
    def parse(self, file):
        raise NotImplementedError()

    def do(self, command):
        if command['cmd'] in self.draw_degrees:
            command['operand'].insert(0, self.draw_degrees[command['cmd']])
        self.draw_methods[command['cmd']](*command['operand'])
