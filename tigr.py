"""Tigr.

Usage:
  tigr.py [FILE ...] [-e tkinter] [-s 5] [--pen-color black]

Options:
  -h --help                  Show this screen.
  -e turtle --engine turtle  Specify the drawer engine, tkinter or turtle. [default: turtle]
  -s 5 --speed 5             Specify the drawer speed, 1 slowest, 9 fastest [default: 5]
  --pen-color black          Specify pen color [default: black]
  --version                  Show version
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Tigr 1.0')
    print(arguments)

    import tigr
    tigr.main(arguments)