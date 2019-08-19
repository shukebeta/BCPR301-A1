
def main(arguments):
    # default interactive mode
    # support stdin
    # default turtle_worker
    # before execute input instructs, draw a star as welcome figure
    import tigr.shell.cmd as cmd

    from tigr.drawer.drawer import Drawer

    if arguments['--engine'] != 'turtle':
        from tigr.drawer.tkinter_worker import TkinterWorker as Worker
    else:
        from tigr.drawer.turtle_worker import TurtleWorker as Worker

    worker = Worker(
        speed=int(arguments['--speed']),
        pencolor=arguments['--pencolor'],
        pensize=arguments['--pensize'],
    )
    drawer = Drawer(worker)
    if len(arguments['FILES']) > 0:
        from tigr.parser.regex_parser import RegexParser as Parser
        parser = Parser(drawer)
        for afile in arguments['FILES']:
            with open(afile) as file:
                parser.parse(file)

        import time
        time.sleep(0.5)
        if arguments['--interactive'] == '1':
            import tigr.shell.cmd as cmd
            cmd.Shell(drawer).cmdloop()
    else:
        cmd.Shell(drawer).cmdloop()
