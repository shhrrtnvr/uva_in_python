for _ in range(int(input())):
    Board = [[(weight, j) for j, weight in enumerate(map(int, input().split()))] for i in range(8)]
    for row in Board:
        row.sort(reverse=True)
    RowMax = [row[0][0] for row in Board]
    best = sum([row[-1][0] - row[0][0] for row in Board])
    ans = None
    taken = []
    def backtrack(gain):
        i = len(taken)
        if i == 8:
            global ans
            ans = taken[:]
            global best
            best = gain
            return 
        for weight, j in Board[i]:
            flag = False
            for r, c in taken:
                if c==j or abs(i-r) == abs(j-c):
                    flag = True
                    break
            if flag: continue
            newgain = gain+weight-RowMax[i]
            if newgain < best:
                return 
            taken.append((i, j))
            backtrack(newgain)
            taken.pop()
        return 
    backtrack(0)
    print('%5d' %(sum(RowMax)+best))


