import sys
sum = 0
while True:
    try:
        line = input()      # or call sys.stdin.readlines()
    except EOFError:        # or for line in sys.stdin:
        break               # input strip \n at end
    else:
        sum += int(line)
print(sum)