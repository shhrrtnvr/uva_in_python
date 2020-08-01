for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    if 1<<n  == m:
        print(0)
        input()
        continue
    withdraw = set(map(lambda x: int(x)-1, input().rstrip().split()))
    nxt = set()
    total = 0
    while withdraw:
        for w in withdraw:
            if w^1 in withdraw:
                nxt.add(w>>1)
            else:
                total += 1
        withdraw.clear()
        withdraw, nxt = nxt, withdraw
    print(total)