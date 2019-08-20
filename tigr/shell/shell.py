import cmd, sys

class Shell(cmd.Cmd):
    intro = 'Welcome to the tigr shell.   Type help or ? to list commands.\n'
    file = None

    def __init__(self, drawer):
        self.drawer = drawer
        self.prompt = 'current drawer: ' + drawer.worker.__name__ + '> '
        super().__init__()
        self.alias_list = {
            'quit': self.do_bye,
            'd': self.do_pendown,
            'u': self.do_penup,
            'dl': self.do_draw_line,
        }

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        if cmd in self.alias_list:
            return self.alias_list[cmd](arg)
        else:
            super().default(line)

    # ----- basic turtle commands -----

    def do_select_pen(self, arg):
        self.drawer.select_pen(*parse_int(arg))

    def do_penup(self, arg):
        self.drawer.pen_up()

    def do_pendown(self, arg):
        self.drawer.pen_down()

    def do_pencolor(self, arg):
        self.drawer.pencolor(*parse(arg))

    def do_pensize(self, arg):
        self.drawer.pensize(*parse_int(arg))

    def do_go_along(self, arg):
        self.drawer.go_along(*parse_int(arg))

    def do_goto(self, arg):
        self.drawer.goto(*parse_int(arg))

    def do_go_down(self, arg):
        self.drawer.go_down(*parse_int(arg))

    def do_forward(self, arg):
        self.drawer.forward(*parse_int(arg))

    def do_draw_line(self, arg):
        self.drawer.draw_line(*parse_int(arg))

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print(f'Thank you for using {self.drawer.worker.__name__}')
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
    return tuple(arg.split())

def parse_int(arg):
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    from tigr.drawer.drawer import Drawer
    from tigr.drawer.tkinter_worker import TkinterWorker
    Shell(Drawer(TkinterWorker())).cmdloop()        