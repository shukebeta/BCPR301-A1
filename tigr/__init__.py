def main():
    # default interactive mode
    # support stdin
    # default turtle_worker
    # before execute input instructs, draw a star as welcome figure
    import tigr.shell.cmd as cmd
    import turtle
    cmd.Shell(turtle).cmdloop()