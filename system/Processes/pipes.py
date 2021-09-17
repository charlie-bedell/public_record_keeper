"""
spawn a child process/program, connect my stdin/stdout to child process's
stdout/stdin--my reads and writes map to output and input stream of the
spawned program; much like tying together streams with subprocess module;
"""

import os, sys

def spawn(prog, *args):                             # pass progname, cmdline args
    stdinFd = sys.stdin.fileno()                    # get descriptors for streams
    stdoutFd = sys.stdout.fileno()                  # normally stdin=0, stdout=1

    parentStdin, childStdout = os.pipe()            # make two IPC pipe channels
    childStdin, parentStdout = os.pipe()            # pipe returns (inputfd, outputfd)
    pid = os.fork()
    if pid:
        os.close(childStdout)                       # in parent process after fork:
        os.close(childStdin)                        # close chuld ends in parent
        os.dup2(parentStdin, stdinFd)               # my sys.stdin copy  = pipe1[0]
        os.dup2(parentStdout, stdoutFd)             # my sys.stdin copy  = pipe2[1]
    else:
        os.close(parentStdin)                       # in child process after fork:
        os.close(parentStdout)                      # close parent ends in child
        os.dup2(childStdin, stdinFd)                # my sys.stdin copy  = pipe1[0]
        os.dup2(childStdout, stdoutFd)              # my sys.stdin copy  = pipe2[1]
        args = (prog,) + args
        os.execvp(prog, args)                       # new program in this process
        assert False, 'execvp failed!'              # os.exec call never returns here

if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', 'pipes-testchild.py', 'spam')   # for child program
    
    print('Hello 1 from parent', mypid)             # to child's stdin
    sys.stdout.flush()                              # subvert stdio buffering
    reply = input()                                 # from childs stdout
    sys.stderr.write(f'Parent got: {reply[:-1]}')   # stderr not tied to pipe!

    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = input()
    sys.stderr.write(f'Parent got: {reply[:-1]}')
