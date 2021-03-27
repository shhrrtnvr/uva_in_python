while True:
    b, n = map(int, input().split())
    if b == 0 and n == 0:
        break
    bank = list(map(int, input().split()))
    for _ in range(n):
        d, c, a = map(int, input().split())
        d, c = d-1, c-1
        bank[d] -= a
        bank[c] += a
    for bal in bank:
        if bal < 0:
            print('N')
            break
    else:
        print('S')