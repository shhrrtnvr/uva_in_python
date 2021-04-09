adj = list()
def build(n):
    adj.clear()
    f = lambda x : int(x)-1
    for _ in range(n):
        adj.append(list(map(f, input().split()[1:])))

from collections import defaultdict
dp = defaultdict(lambda : [0, 1])

def dfs(u, p):
    for v in adj[u]:
        if v != p:
            dfs(v, u)
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v])

while True:
    n = int(input())
    if n == 0:
        break
    build(n)
    dp.clear()
    dfs(0, -1)
    print(max(1,min(dp[0])))
