import cmd, sys

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

    def default(self, line):
        try:
            # process P9 / X-100 similar commands
            line = line.strip()
            if len(line) >= 2 and (line[1] == '-' or line[1] in [str(i) for i in range(0,10)]):
                line = line[0] + ' ' + line[1:]

            # process comments
            index = line.find('#')
            if index != -1:
                line = line[:index]

            cmd, arg, line = self.parseline(line)
            cmd = cmd.lower()
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

    # ----- basic turtle commands -----

    def do_select_pen(self, arg):
        "Select a pen: 1 ~ 9"
        self.drawer.select_pen(*parse_int(arg))

    def do_penup(self, Pearg):
        "Set pen up, other draw instructions except draw_line will just move but don't draw."
        self.drawer.pen_up()

    def do_pendown(self, arg):
        "Set pen down, draw instructions except goto will move and draw."
        self.drawer.pen_down()

    def do_pencolor(self, arg):
        "Set pen color: green, orange or any other colors"
        self.drawer.pencolor(*parse(arg))

    def do_pensize(self, arg):
        "Set pen size: 1 ~ 9"
        self.drawer.pensize(*parse_int(arg))

    def do_go_along(self, arg):
        "Draw a horizontal line of a specified length"
        self.drawer.go_along(*parse_int(arg))

    def do_goto(self, arg):
        "Goto a position without drawing any line"
        self.drawer.goto(*parse_int(arg))

    def do_go_down(self, arg):
        "Draw a vertical line of a specified length"
        self.drawer.go_down(*parse_int(arg))

    def do_forward(self, arg):
        "Move specified distance along the original heading"
        self.drawer.forward(*parse_int(arg))

    def do_draw_line(self, arg):
        "Draw a line with specified degree and distance"
        self.drawer.draw_line(*parse_int(arg))

    def do_bye(self, arg):
        'Close the drawing window and exit:  BYE'
        print(f'Thank you for using {self.drawer.worker.name}')
        self.drawer.bye()
        return True

    # def __getattr__(self, item):
    #     alias = {
    #         'do_quit': self.do_bye
    #     }
    #     if item in alias:
    #         return alias[item]



def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return arg.split()

def parse_int(arg):
    return map(int, arg.split())

if __name__ == '__main__':
    from tigr.drawer.drawer import Drawer
    from tigr.drawer.tkinter_worker import TkinterWorker
    Shell(Drawer(TkinterWorker())).cmdloop()