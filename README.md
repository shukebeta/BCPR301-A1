# BCPR301-A1
BCPR301 Advanced Programming Assignment 1:  Extend the provided the Tiny Interpreted Graphics language package (TIGr) to give it more flexibility, functionality, robustness and portability. 

In this project, we plan to implement below features:

1. Cmd interface for TIGr (mostly a shell interface)
2. Support piping and scripting
3. Command line switches
4. Parsed from configurable lookup table
5. Regular Expression Parser
6. Generic Parser
7. Tkinter output
8. Turtle output
9. Several doctest case (great than 5)
10. Several unitest case (great than 5)

It is a shell application which supports multiple drawer engine, include Turtle, TkInter.

- This shell supports below command line switches:
    - --pen-size: default 'default'
    - --pen-color: default 'black'
    - -s --speed: default 5 (1 slowest 9 fastest)
    - -e or --engine: default 'turtle'
    - -c or --config-file: default 'config.ini'
    - --run-test

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
    - unittest
    
- Usage:
    - python tigr.py # interactive mode, with default parameters
    - python tigr.py < instructions.txt
    - python tigr.py --pen-color=red 
    - python tigr.py --engine=tkinter
    - ptyhon tigr.py --run-test
    - python tigr.py ins1.txt ins2.txt ins3.txt
         
 
