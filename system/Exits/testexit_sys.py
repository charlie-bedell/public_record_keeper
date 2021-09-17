def later():
    import sys
    print('bye sys world')
    sys.exit(42)
    print('never reached')

if __name__ == '__main__': later()