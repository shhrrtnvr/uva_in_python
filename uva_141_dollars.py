coins = (0, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000)

dp = [[0] * (len(coins) + 1) for _ in range(30001)]
dp[0][0] = 1
for i in range(1, len(coins)):
    for v in range(1, 30001):
            k = v
        while k > 0:
            dp[v][i] += dp[k][i-1]
            k -= coins[i]

while True:
    try:
        val = int(float(input()) * 100)
        print(val)
        print(dp[val][len(coins)-1])
    except:
        exit()


