import string
class tree:
    def __init__(self):
        self.size = 26
        self.field = {x:[x, 1, 1] for x in string.ascii_uppercase}
    def parent(self, x):
        p = self.field[x][0]
        if p == x:
            return x
        else:
            p = self.field[x][0] = self.parent(p)
            return p

    def edge(self, u, v):
        pu, pv = self.parent(u), self.parent(v)
        if pu == pv:
            self.size -= self.field[pu][2]
            self.field[pu][2] = 0
        else:
            if self.field[pu][1] < self.field[pv][1]:
                pu, pv = pv, pu
            self.field[pv][0] = pu
            self.field[pu][1] += self.field[pv][1]
            self.field[pu][2] = min(self.field[pu][2], self.field[pv][2])
            self.size -= max(self.field[pu][2], self.field[pv][2])
    
    def numoftree(self):
        return self.size

tc = int(input())
for _ in range(tc):
    forest = tree()
    nodes = set()
    while True:
        l = input()
        if l[0] == '*': break
        forest.edge(l[1], l[3])
        nodes |= {l[1], l[3]}
    all = set(input().rstrip().split(','))
    print('There are %d tree(s) and %d acorn(s).' %(forest.numoftree()+len(nodes)-26, len(all-nodes)))
    
