tc = int(input())
for _ in range(tc):
    edge, vertex = 0, set()
    while True:
        l = input()
        if l[0] == '*': break
        vertex |= {l[1], l[3]}
        edge += 1
    print('There are %d tree(s) and %d acorn(s).' %(len(vertex) - edge, len(set(input().split(',')) - vertex)))
