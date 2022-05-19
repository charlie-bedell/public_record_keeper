"""
Find the largest Python source file in an entire directory tree.
Search the python source lib, use pprint to display results nicely.
"""

import sys, os, pprint

trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python31\Lib'            # Windows
else:
    dirname = '/usr/lib/python'             # Unix, Linux, Cygwin

if len(sys.argv) > 1:
    dirname = f'{os.path.abspath(os.getcwd())}\\' + str(sys.argv[1])

print(dirname)

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if trace: print('...', filename)
        fullname = os.path.join(thisDir, filename)
        fullsize = os.path.getsize(fullname)
        allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])

if len(sys.argv) > 1:
    sys.argv[1]