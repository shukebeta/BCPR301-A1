def main():
    # default interactive mode
    # support stdin
    # default turtle_worker
    # before execute input instructs, draw a star as welcome figure
    from shell import cmd
    import turtle
    cmd.Shell(turtle).cmdloop()
    pass