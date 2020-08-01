for _ in range(int(input())):
    m, n = map(int, input().split())
    A, edge, flag = [[] for _ in range(n)], set(), True
    for r in range(m):
        l = input()
        if flag:
            l = l.split()
            if len(l) != n: flag = False; continue
            for i, v in enumerate(l):
                if v == '1': 
                    A[i].append(r)
                    if len(A[i]) == 2:
                        if tuple(A[i]) in edge: 
                            flag = False; break
                        else:
                            edge.add(tuple(A[i]))
                    elif len(A[i]) > 2: flag = False; break
    if flag:
        for v in A:
            if len(v) == 1: flag = False; break
    print('Yes' if flag else 'No')
    


