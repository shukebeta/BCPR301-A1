import os

from tigr.drawer.tkinter_worker_factory import TkInterWorkerFactory
from tigr.drawer.turtle_worker_factory import TurtleWorkerFactory

os.environ['TK_SILENCE_DEPRECATION'] = '1'



def main(arguments):
    # default interactive mode
    # support stdin
    # default turtle_worker
    # before execute input instructs, draw a star as welcome figure
    import tigr.shell.shell as cmd

    from tigr.drawer.drawer import Drawer

    if arguments['--engine'] != 'turtle':
        worker = TkInterWorkerFactory().create_worker()
    else:
        worker = TurtleWorkerFactory().create_worker()

    worker.speed(int(arguments['--speed']))
    worker.pencolor(arguments['--pencolor'])
    worker.pensize(arguments['--pensize'])

    drawer = Drawer(worker)
    if len(arguments['FILES']) > 0:
        if arguments['--parser'] == 'regex':
            from tigr.parser.regex_parser import RegexParser as Parser
        else:
            from tigr.parser.peg_parser import PEGParser as Parser
        from tigr.reader.reader import SourceReader

        parser = Parser(drawer)
        for filename in arguments['FILES']:
            reader = SourceReader(parser, filename)
            reader.go()

        import time
        time.sleep(0.5)
        if arguments['--interactive']:
            from tigr.shell.shell import Shell
            Shell(drawer).cmdloop()
    else:
        cmd.Shell(drawer).cmdloop()
