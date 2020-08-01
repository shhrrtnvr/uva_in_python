import math
while True:
    n = int(input())
    if n == 0: break
    total, mini = 0, math.inf
    for _ in range(n):
        space = 25-input().count('X')
        total += space
        mini = min(mini, space)
    print(total - mini * n)

