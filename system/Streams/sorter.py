import sys                              # or sorted(sys.stdin)
lines = sys.stdin.readlines()           # sort stdin input lines,
lines.sort()                            # send results to stdout
for line in lines: print(line, end='') # for further processing