
def main(engine='turtle'):
    # default interactive mode
    # support stdin
    # default turtle_worker
    # before execute input instructs, draw a star as welcome figure
    import tigr.shell.cmd as cmd

    from tigr.drawer.drawer import Drawer

    if engine != 'turtle':
        from tigr.drawer.tkinter_worker import TkinterWorker as Worker
    else:
        from tigr.drawer.turtle_worker import TurtleWorker as Worker

    cmd.Shell(Drawer(Worker())).cmdloop()
