
def main():
    # default interactive mode
    # support stdin
    # default turtle_worker
    # before execute input instructs, draw a star as welcome figure
    import tigr.shell.cmd as cmd
    import turtle

    from tigr.drawer.drawer import Drawer
    cmd.Shell(Drawer(turtle)).cmdloop()