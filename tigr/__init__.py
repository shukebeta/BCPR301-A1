
def main():
    # default interactive mode
    # support stdin
    # default turtle_worker
    # before execute input instructs, draw a star as welcome figure
    import tigr.shell.cmd as cmd
    import turtle

    from tigr.drawer.drawer import Drawer

    if 0:
        from tigr.drawer.tkinter_worker import TkinterWorker as Worker
    else:
        from tigr.drawer.turtle_worker import TurtleWorker as Worker

    cmd.Shell(Drawer(Worker())).cmdloop()
