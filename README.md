# BCPR301-A1
BCPR301 Advanced Programming Assignment 1:  Extend the provided the Tiny Interpreted Graphics language package (TIGr) to give it more flexibility, functionality, robustness and portability. 

In this project, we plan to implement below features:

1. Cmd interface for TIGr: a shell similar interpreter
2. Support piping and scripting
3. Command line switches
4. Parsed from configurable lookup table
5. Regular Expression Parser
6. Generic Parser
7. Tkinter output
8. Turtle output
9. Several doctest case: 20 test case for tkinter-worker
10. Several unitest case: 10 test case for tkinter-worker
11. Recording drawing instructions
12. Playback for recorded drawing instructions
13. Reset canvas
14. Exceptions process for robustness  

It is a shell application which supports multiple drawer engine, include Turtle, TkInter.

- This shell supports below command line switches:
    - --pensize 2: default 1
    - --pencolor red: default 'black'
    - -s --speed 999: default 7 (0 slowest 9999 fastest)
    - -e or --engine tkinter: default 'turtle'
    - -c or --config 1.ini
    - --runtest

- This shell support two running mode

    - interactive mode: shell mode
        1. it can get instructions from pipe
        2. it can get instructions from user input
    - batch mode: read script file and auto draw something
        1. support space separated multiple scripts file at command line

- This shell application support two types of config file
    - config.ini
    - config.yaml 

- This application includes test
    - doctest
        - `python -m doctest -v tigr/drawer/tkinter_worker.py`
    - unittest
        - `python -m unittest discover tigr/test`
- Usage:
    - python tigr.py # interactive mode, with default parameters
    - python tigr.py < instructions.txt
    - python tigr.py --pencolor=red 
    - python tigr.py --engine=tkinter
    - ptyhon tigr.py --runtest
    - python tigr.py ins1.txt ins2.txt ins3.txt
         
 
