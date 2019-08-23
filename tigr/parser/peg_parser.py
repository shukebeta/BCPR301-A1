from parsimonious.grammar import Grammar
from tigr.parser.regex_parser import RegexParser
from tigr.parser.visitor import Visitor
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PEGParser(RegexParser):
    grammer = Grammar(
        r"""
        expr    = zero / one / two / comment
        zero    = ws* ~'([DU])'i comment?
        two     = ws* ~'(G|L)'i ws* (operand) ws+ (operand) comment?
        one     = ws* ~'([PNSEWXY])'i ws* (operand) comment?
        operand = ~r'-?[0-9]+'
        ws      = ~"\s"
        comment = ws* "#" ~r'.*'
        """
    )

    visitor = Visitor()

    def parse(self, file):
        for line in file:
            line = line.strip()
            if line == '': continue
            try:
                cmd_tree = self.grammer.parse(line)
                cmd = self.visitor.visit(cmd_tree)
                if cmd[0] == '#':
                    print(f'comment found: "{"".join(cmd)}"')
                else:
                    command = {
                        'cmd': cmd[0].upper(),
                        'operand': [int(i) for i in cmd[1:]]
                    }
                    self.do(command)
            except Exception as e:
                print(f'Invalid command: {line}')
                logger.debug(e)


if __name__ == '__main__':

    from tigr.drawer.drawer import Drawer
    if 1:
        from tigr.drawer.turtle_worker import TurtleWorker as Worker
    else:
        from tigr.drawer.tkinter_worker import TkinterWorker as Worker

    drawer = Drawer(Worker())
    parser = PEGParser(drawer)
    parser.parse(open('../test/instructions2.txt'))

    import time

    time.sleep(0.5)
    from tigr.shell.shell import Shell
    Shell(drawer).cmdloop()