from tigr.parser.abstract_parser import AbstractParser
import re


class RegexParser(AbstractParser):
    pattern = r'^([DUPNESWXYGL])\s*(-?[\s\d]+)?(?:#.*)?$'
    p = re.compile(pattern, re.IGNORECASE)

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

    def parse(self, file):
        self.drawer.reset()
        for line in file:
            line = line.strip()
            if line != '':
                cmd = self.parseline(line)
                if cmd['error_message']:
                    print(cmd['error_message'])
                else:
                    self.do(cmd['command'])

    def do(self, command):
        return self.drawer.do_draw_command(command['cmd'], command['operand'])


if __name__ == '__main__':

    from tigr.drawer.drawer import Drawer
    if 1:
        from tigr.drawer.turtle_worker_factory import TurtleWorkerFactory as Factory
    else:
        from tigr.drawer.tkinter_worker_factory import TkInterWorkerFactory as Factory

    drawer = Drawer(Factory().create_worker())
    parser = RegexParser(drawer)
    parser.parse(open('../test/instructions2.txt'))

    import time

    time.sleep(0.5)

    from tigr.shell.shell import Shell

    Shell(drawer).cmdloop()
