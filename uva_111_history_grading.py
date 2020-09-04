import math
import bisect

n = None
while True:
    try:
        line = list(map(int, input().rstrip().split()))
    except:
        break
    if len(line) != n:
        n = line[0]
        ranking = list(map(int, input().rstrip().split()))
        continue

    student_ranking = line
    student_ordering = [None] * n
    lis_len = 0
    for i, rank in enumerate(map(int, student_ranking)):
        try:
            student_ordering[rank-1] = i
        except:
            print('error', rank)
            break
    dp = [-math.inf] + [math.inf]*(n+1)
    for event in student_ordering:
        pos = bisect.bisect_left(dp, ranking[event])
        dp[pos] = ranking[event]
        lis_len = max(lis_len, pos)
    print(lis_len)