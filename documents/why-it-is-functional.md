# Why it is functional

## It supports below instructions:

    U                   set pen up
    D                   set pen down
    G  x y              goto x y    (position)
    N  distance         draw line toward North (up)
    S  distance         draw line toward  South (down)
    E  distance         draw line toward  East (left)
    W  distance         draw line toward  West (right)
    X  distance         draw line along x axis 
    Y  distance         draw line down y axis 
    L  degree distance  draw line certain with distance at certain degree

## It has a powerful shell (interpreter)

You can use all short format instructions in the shell.

You can also use below long format instructions：

    penup                   set pen up
    pendown                 set pen down
    pencolor                set pen color
    pensize                 set pen size
    select_pen              select pen
    goto                    goto position
    get_along               go along x axis
    go_down                 go along y axis
    forward                 go along original direction
    draw_line               draw line with 
    reset                   clear all the drawing
    record                  record instructions to file
    playback                playback from instructions file
    bye                     good bye
    

## It supports two drawing engine:

- tkinter
- turtle

## It supports two type of configuration file

- ini file
- yaml file 

## It can run in multiple ways 

It can run as an interpreter, a batch instructions processor, and a command line application supports 
below arguments and options:

    Tigr.
    
    Usage:
      tigr.py [FILES ...] [-c c.ini] [-e tkinter] [-s 5] [-p regex] [--pencolor black] [--pensize 1] [-i]
    
    You can also run all the unittest by this command: python -m unittest discover tigr/test
    You can also run all the doc-test by this command: python -m doctest -v tigr/drawer/tkinter_worker.py
    
    Options:
      -h --help                  Show this screen.
      -c 1.ini --config 1.ini    Specify the ini config file name
      -e turtle --engine turtle  Specify the drawer engine, tkinter or turtle. [default: turtle]
      -s 5 --speed 5             Specify the drawer speed, 1 slowest, 9 fastest [default: 5]
      -p regex --parser regex    Specify the instruction parser [default: peg]
      --pencolor black           Specify pen color [default: black]
      --pensize 1                Specify pen size [default: 1]
      -i --interactive           Specify if enter interactive mode when the script files were executed done [default: 0]
      --version                  Show version
    
    Attention:
    
    If an option is found in config file and command line arguments at the same time,
    this program will use the value from the ini file.

## Typical use scenario

### As an interpreter

    python tigr.py 
    
### As a batch processor
    
    python tigr.py < tigr/test/test-instructions.txt
    
### As a command line application

   python tigr.py -c config.ini -e tkinter --pencolor red --pensize 2 --speed 9 tigr/test/instructions{2,1}.txt
