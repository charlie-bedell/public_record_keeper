"""
anonymous pipes and threads, not processes; this version works on Windows
"""

# NOTE at least on this programs' threads may not die on ctrl-C, you may need to kill it in the task manager

import os, time, threading

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                         # make parent wait
        msg = (f'Spam 00{zzz}').encode()        # pipes are binary bytes
        os.write(pipeout, msg)                  # send to parent
        zzz = (zzz + 1) % 5                     # goto 0 after 4


def parent(pipein):
    while True:
        line = os.read(pipein, 32)
        print(f'Parent {os.getpid()} got [{line}] at {time.time()}')


pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)