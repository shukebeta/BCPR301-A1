import cmd
import os


class Shell(cmd.Cmd):
    intro = 'Welcome to the tigr shell.   Type help or ? to list commands.\n'
    file = None

    def __init__(self, drawer):
        self.drawer = drawer
        self.prompt = 'current drawer: ' + drawer.worker.name + '> '
        super().__init__()
        self.alias_list = {
            'quit': self.do_bye,
            'd': self.do_pendown,
            'u': self.do_penup,
            'l': self.do_draw_line,
            'g': self.do_goto,
            'p': self.do_select_pen,
            'x': self.do_go_along,
            'y': self.do_go_down,
        }

        self.heading_dict = {
            'n': 90,
            's': 270,
            'e': 0,
            'w': 180,
        }

        self.path_file = ''
        self.recording = False

    def precmd(self, line):
        line = line.lower()
        if self.recording and 'playback' not in line:
            with open(self.path_file, 'a') as f:
                print(line, file=f)

        # process P9 / X-100 similar commands
        line = line.strip()
        if len(line) >= 2 and (line[1] == '-' or line[1] in [str(i) for i in range(0, 10)]):
            line = line[0] + ' ' + line[1:]

        # process comments
        index = line.find('#')
        if index != -1:
            line = line[:index]
        return line

    def default(self, line):
        try:
            cmd, arg, line = self.parseline(line)
            if cmd in self.alias_list:
                return self.alias_list[cmd](arg)
            elif cmd in ['n', 's', 'e', 'w']:
                arg = f'{self.heading_dict[cmd]} {arg}'
                self.do_draw_line(arg)
            else:
                # process EOF
                if line == 'EOF':
                    import time
                    time.sleep(0.5)
                    raise SystemExit
                # getattr(self, f'do_{cmd}')(arg)
                super().default(line)
        except Exception as e:
            print(f'Invalid command {line}')

    def emptyline(self):
        pass

    # ----- basic commands -----

    def do_select_pen(self, arg):
        """Select a pen: 1 ~ 9"""
        self.drawer.select_pen(*parse_int(arg))

    def do_penup(self, arg):
        """Set pen up, other draw instructions except draw_line will just move but don't draw."""
        self.drawer.pen_up()

    def do_pendown(self, arg):
        """Set pen down, draw instructions except goto will move and draw."""
        self.drawer.pen_down()

    def do_pencolor(self, arg):
        """Set pen color: green, orange or any other colors"""
        self.drawer.pencolor(*parse(arg))

    def do_pensize(self, arg):
        """Set pen size: 1 ~ 9"""
        self.drawer.pensize(*parse_int(arg))

    def do_go_along(self, arg):
        """Draw a horizontal line of a specified length"""
        self.drawer.go_along(*parse_int(arg))

    def do_goto(self, arg):
        """Goto a position without drawing any line"""
        self.drawer.goto(*parse_int(arg))

    def do_go_down(self, arg):
        """Draw a vertical line of a specified length"""
        self.drawer.go_down(*parse_int(arg))

    def do_forward(self, arg):
        """Move specified distance along the original heading"""
        self.drawer.forward(*parse_int(arg))

    def do_draw_line(self, arg):
        "Draw a line with specified degree and distance"
        self.drawer.draw_line(*parse_int(arg))

    def do_reset(self, arg):
        self.drawer.reset()

    def do_bye(self, arg):
        'Close the drawing window and exit:  BYE'
        self.close()
        self.drawer.bye()
        print(f'Thank you for using {self.drawer.worker.name}')
        return True

    # def __getattr__(self, item):
    #     alias = {
    #         'do_quit': self.do_bye
    #     }
    #     if item in alias:
    #         return alias[item]

   # ----- record and playback -----
    def do_record(self, arg):
        """Save future commands to filename:  RECORD rose.cmd"""
        path_file = arg.strip()
        if path_file == '':
            print('You need a filename after your command.')
            return None
        else:
            pwd = os.path.dirname(os.path.abspath(__file__))
            self.path_file = f'{pwd}{os.sep}..{os.sep}test{os.sep}{arg}'

        # truncate path_file to zero length
        open(self.path_file, 'w').close()
        self.recording = True

    def do_playback(self, arg):
        """Playback commands from a file:  PLAYBACK rose.cmd"""
        self.recording = False
        self.drawer.reset()

        path_file = arg.strip()
        if path_file == '':
            if self.path_file != '':
                path_file = self.path_file
            else:
                print('You need a filename after your command.')
                return None
        else:
            pwd = os.path.dirname(os.path.abspath(__file__))
            path_file = f'{pwd}{os.sep}..{os.sep}test{os.sep}{arg}'

        try:
            with open(path_file) as f:
                instructions = f.read()
                self.cmdqueue.extend(instructions.splitlines())
                f.close()
        except Exception as e:
            print(e)

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return arg.split()

def parse_int(arg):
    return map(int, arg.split())

if __name__ == '__main__':
    from tigr.drawer.drawer import Drawer
    from tigr.drawer.tkinter_worker import TkinterWorker
    Shell(Drawer(TkinterWorker())).cmdloop()
