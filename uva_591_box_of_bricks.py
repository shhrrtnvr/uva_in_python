from functools import reduce
from itertools import count
n = count(1, 1)
while True:
    stack = int(input())
    if not stack: break
    bricks = list(map(int,input().strip().split()))
    height = sum(bricks) // stack
    print('Set #{}'.format(next(n)))
    print('The minimum number of moves is {}.'.format(reduce(lambda x, y: x+abs(height-y), bricks, 0)//2))
    print()

