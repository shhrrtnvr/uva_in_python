t = 0
while True:
    t += 1
    n = int(input())
    if n == 0: break
    print('Case #%d:' %t)
    data = []
    start = 0
    for _ in range(n):
        y, a, b = map(int, input().split())
        if y > start:
            start = y
        data.append((y, b-a))
    for year in range(start, 10000, 1):
        for y, d in data:
            if (year - y) % d != 0:
                break
        else:
            print('The actual year is %d.' %year)
            break
    else:
        print('Unknown bugs detected.')
    print()



