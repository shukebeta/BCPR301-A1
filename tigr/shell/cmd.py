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
        }

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        if cmd in self.alias_list:
            return self.alias_list[cmd](arg)
        else:
            super().default(line)

    # ----- basic turtle commands -----

    def do_select_pen(self, arg):
        self.drawer.select_pen

    def do_penup(self, arg):
        self.drawer.pen_up()

    def do_pendown(self, arg):
        self.drawer.pen_down()

    def do_pencolor(self, arg):
        self.drawer.pen_color(*parse(arg))

    def do_go_along(self, arg):
        self.drawer.go_along(*parse(arg))

    def do_go_down(self, arg):
        self.drawer.go_down(*parse(arg))

    def do_draw_line(self, arg):
        self.drawer.draw_line(*parse(arg))

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print(f'Thank you for using {self.drawer.worker.__name__}')
        self.close()
        self.drawer.bye()
        return True

    # def __getattr__(self, item):
    #     alias = {
    #         'do_quit': self.do_bye
    #     }
    #     if item in alias:
    #         return alias[item]


    # ----- record and playback -----
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(arg.split())
