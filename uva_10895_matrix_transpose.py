while True:
    try: m, n = map(int, input().rstrip().split())
    except: break
    Ti = [[] for _ in range(n)]
    Tv = [[] for _ in range(n)]
    for i in range(m):
        col = map(int, input().rstrip().split())
        val = input()
        if next(col) == 0: continue
        for v in val.rstrip().split():
            ri = next(col)-1
            Ti[ri].append(i+1)
            Tv[ri].append(v)
    print(n, m)
    for index, vals in zip(Ti, Tv):
        print(' '.join(map(str,[len(index)]+index)))
        print(' '.join(vals))
        
