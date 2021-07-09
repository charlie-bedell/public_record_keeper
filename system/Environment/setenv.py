import os
print('setenv...', end=' ')
print(os.environ['USERNAME'])       # show current shell variable value

os.environ['USERNAME'] = 'Brian'    # runs os.putenv behind the scenes
os.system('python echoenv.py')

os.environ['USERNAME'] = 'Arthur' # changes passed to spawned programs
os.system('python echoenv.py')  # and linked-in C library modules

os.environ['USERNAME'] = input('?')
print(os.popen('python echoenv.py').read())