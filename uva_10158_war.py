class UF:
    def __init__(self, n):
        self.P = [i for i in range(n+1)]
        self.W = [1 for i in range(n+1)]
    def parent(self, x):
        if self.P[x] == x:
            return x
        p = None
        if self.P[x] > 0:
            p = self.parent(self.P[x])
        else :
            p = -self.parent(-self.P[x])
        self.P[x] = p
        return p

    def areFriends(self, x, y):
        return self.parent(x) == self.parent(y)
    
    def areEnemies(self, x, y):
        return self.parent(x) == -self.parent(y)
    
    def setFriends(self, x, y):
        if self.areEnemies(x, y): return -1
        if not self.areFriends(x, y):
            px, py = self.parent(x), self.parent(y)
            sx, sy = 1 if px > 0 else -1, 1 if py > 0 else -1
            if self.W[sx*px] > self.W[sy*py]:
                self.P[sy*py] = sy*px
                self.W[sx*px] += self.W[sy*py]
            else:
                self.P[sx*px] = sx*py
                self.W[sy*py] += self.W[sx*px]

    def setEnemies(self, x, y):
        if self.areFriends(x, y): return -1
        if not self.areEnemies(x, y):
            px, py = self.parent(x), self.parent(y)
            sx, sy = 1 if px > 0 else -1, 1 if py > 0 else -1
            if self.W[sx*px] > self.W[sy*py]:
                self.P[sy*py] = -sy*px
                self.W[sx*px] += self.W[sy*py]
            else:
                self.P[sx*px] = - sx*py
                self.W[sy*py] += self.W[sx*px]
    

if __name__ == '__main__':
    n = int(input())
    relation = UF(n)
    while True:
        c, x, y = map(int, input().rstrip().split())
        x, y = x+1, y+1
        if c == 0: break
        elif c == 1:
            if relation.setFriends(x, y) == -1: print(-1)
        elif c == 2:
            if relation.setEnemies(x, y) == -1: print(-1)
        elif c == 3:
            print(1 if relation.areFriends(x, y) else 0)
        elif c == 4:
            print(1 if relation.areEnemies(x, y) else 0)
        