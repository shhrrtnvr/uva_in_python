import heapq
def calc(s): 
    start, end = {}, {}
    for i, ship in enumerate(s):
        if ship in start:
            end[ship] = i
        else:
            start[ship], end[ship] = i, i
    pq = []
    for ship in start:
        heapq.heappush(pq, (start[ship], ship, 'start'))
        heapq.heappush(pq, (end[ship], ship, 'end'))
    n = 0
    stack = set()
    while pq:
        time, ship, state = heapq.heappop(pq)
        if state == 'start':
            for exist in stack:
                if ship < exist:
                    stack.remove(exist)
                    break
            else:
                n += 1
        else:
            stack.add(ship)
    return n

i = 0
while True:
    containers = input().rstrip()
    if containers == 'end': break
    i += 1
    print('Case %d:' %i, calc(containers))
    
