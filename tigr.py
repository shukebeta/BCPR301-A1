"""Tigr.

Usage:
  tigr.py [-e tkinter]
  tigr.py [-e turtle]

Options:
  -h --help                  Show this screen.
  -e turtle --engine turtle  Specify the drawer engine, can be tkinter, or turtle. [default: turtle]
  --version                  Show version
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Tigr 1.0')
    print(arguments)

    import tigr
    tigr.main(engine=arguments['--engine'])