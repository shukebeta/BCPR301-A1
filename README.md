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

1. This shell supports below command line switches:

- --pen-size: default 'medium'
- --pen-color: default 'black'
- --draw-speed: default 'medium'
- --engine: default 'turtle'
- --config-file: default 'config.ini'

2. This shell support two running mode

- interactive mode: shell mode
    - it can get instructions from pipe
    - it can get instructions from user input
- batch mode: read script file and auto draw something

3. This shell application support two types of config file
    - config.ini
    - config.yaml 

4. This application includes test
    - doctest
    - unittest
 
