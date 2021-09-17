#!C:\Users\charl\AppData\Local\Programs\Python\Python39\python.exe
from sys import argv
from scanfile import scanner
class UnknownCommand(Exception): pass

def process_line(line):                 # define a function
    if line[0] == '*':                  # applied to each line
        print("Ms.", line[1:-1])
    elif line[0] == '+':
        print("Mr.", line[1:-1])        # strip first and last char: \n
    else:
        raise UnkownCommand(line)       # raise an exception

filename = 'data.txt'
if len(argv) == 2: filename = argv[1]   # allow filename cmd arg
scanner(filename, process_line)         # start the scanner