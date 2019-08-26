# BCPR301-A1
BCPR301 Advanced Programming Assignment 1:  Extend the provided the Tiny Interpreted Graphics language package (TIGr) to give it more flexibility, functionality, robustness and portability. 

In this project, we plan to implement below features:

    1. Cmd interface for TIGr: a shell similar interpreter       Adam Peng, Sini Gao
    2. Support piping and scripting                              Zhong Wei, Sini Gao   
    3. Command line switches                                     Zhong Wei, Adam Peng
    4. Parsed from configurable lookup table                     Adam Peng, Sini Gao
    5. Regular Expression Parser                                 Zhong Wei
    6. Generic Parser: PEG Parser                                Zhong Wei, Louis Lu
    7. Tkinter output                                            Zhong Wei  Sini Gao
    8. Turtle output                                             Adam Peng, Sini Gao
    9. Several doctest case: 20 test case for tkinter-worker     Zhong Wei, Sini Gao, Adam Peng
    10. Several unitest case: 10 test case for tkinter-worker    Zhong Wei, Sini Gao, Adam Peng
    11. Exceptions process for robustness                        Zhong Wei, Sini Gao, Adam Peng
    12. Recording drawing instructions                           Zhong Wei
    13. Playback for recorded drawing instructions               Zhong Wei
    14. Reset canvas                                             Zhong Wei

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
    - python tigr.py < instructions.txt (all platforms)
    - cat instructions.txt | python tigr.py (Linux)
    - type instructions.txt | python tigr.py (Windows)
    - python tigr.py --pencolor red 
    - python tigr.py --pensize 8
    - python tigr.py --speed 7 
    - python tigr.py --engine tkinter
    - python tigr.py ins1.txt ins2.txt ins3.txt
    - python tigr.py -c config.ini
    - python tigr.py -c config.yaml
    
         
 
