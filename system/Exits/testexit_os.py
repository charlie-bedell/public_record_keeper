def outahere():
    import os           # os._exit() is preferred for child processes because its doesn't run through things normally done on a full program exit
    print('Bye os world')
    os._exit(99)        # unlike sys.exit(), os._exit is immune to try clauses
    print('never reached')

if __name__ == '__main__': outahere()
