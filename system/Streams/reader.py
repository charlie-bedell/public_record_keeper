print(f'Got this: "{input()}"')
import sys
data = sys.stdin.readline()[:-1]
print('the meaning of life is', data, int(data)*2)