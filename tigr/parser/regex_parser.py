from tigr.parser.strategy_parser import StrategyParser


class RegexParser(StrategyParser):

    def parse(self, file):
        self.drawer.reset()
        for line in file:
            line = line.strip()
            if line:
                cmd = self.parseline(line)
                if cmd['error_message']:
                    print(cmd['error_message'])
                else:
                    self.do(cmd['command'])


if __name__ == '__main__':

    from tigr.drawer.drawer import Drawer
    if 1:
        from tigr.drawer.turtle_worker import TurtleWorker as Worker

    drawer = Drawer(Worker())
    parser = RegexParser(drawer)
    parser.parse(open('../test/instructions2.txt'))

    import time

    time.sleep(0.5)

    from tigr.shell.shell import Shell

    Shell(drawer).cmdloop()
