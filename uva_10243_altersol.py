adj = list()
def build(n):
    adj.clear()
    f = lambda x : int(x)-1
    for _ in range(n):
        adj.append(list(map(f, input().split()[1:])))

ans = 0
def calc(u, p):
    global ans
    place_guard = False
    for v in adj[u]:
        if v != p:
            place_guard |= calc(v, u)
    if place_guard:
        ans += 1
    return ~place_guard

while True:
    n = int(input())
    if n == 0:
        break
    build(n)
    ans = 0
    calc(0, -1)
    print(max(1,ans))
