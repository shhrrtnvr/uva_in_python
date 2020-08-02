lim = 1000000
A = [None]*lim
A[1] = 1
def calc(n):
    if n < lim:
        if A[n] is None:
            if n & 1:
                A[n] = 1 + calc(3*n+1)
            else:
                A[n] = 1 + calc(n >> 1)
        return A[n]
    return 1 + (calc(3*n+1) if n&1 else calc(n>>1))

res = [None]*4*lim
def build(idx, tl, tr):
    if res[idx] != None:
        return res[idx]
    if tl == tr:
        res[idx] = calc(tr)
        return res[idx]
    tm = (tl+tr)//2
    res[idx] = max(build(idx<<1, tl, tm), build((idx<<1) +1, tm+1, tr))
    return res[idx]

def rmq(idx, tl, tr, l, r):
    if l > r:
        return 0
    if l == tl and r == tr:
        if res[idx] is None:
            build(idx, tl, tr)
        return res[idx]
    tm = (tl + tr)//2
    return max(rmq(idx<<1, tl, tm, l, min(r, tm)), rmq((idx<<1)+1, tm+1, tr, max(tm+1, l), r))
    
while True:
    try: i, j = map(int, input().split())
    except: break
    print(i, j, rmq(1, 1, lim-1, min(i,j), max(i,j)))
