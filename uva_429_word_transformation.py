import math
import sys
import itertools
from queue import Queue

input = sys.stdin.readline


def reachable(prev, word):
    cnt = 0
    for c1, c2 in zip(prev, word):
        if c1 != c2:
            cnt += 1
        if cnt > 1:
            return False
    return True


def input_graph():
    table = {}
    adj_list = []
    idx = itertools.count()
    while True:
        word = input().rstrip()
        if word == '*':
            break
        i = next(idx)
        table[word] = i
        adj_list.append([])
        for prev, j in table.items():
            if len(prev) != len(word):
                continue
            if reachable(word, prev):
                adj_list[i].append(j)
                adj_list[j].append(i)
    return table, adj_list


def shortest_path_distance(adj_list, s, d):
    if s == d:
        return 0
    visited = [False] * len(adj_list)
    dist = [math.inf] * len(adj_list)
    q = Queue()
    q.put(s)
    visited[s] = True
    dist[s] = 0
    while not q.empty():
        v = q.get()
        for adj in adj_list[v]:
            if adj == d:
                return dist[v] + 1
            if visited[adj]:
                continue
            visited[adj] = True
            dist[adj] = dist[v] + 1
            q.put(adj)
    return False


if __name__ == '__main__':
    for tc in range(int(input())):
        if tc == 0:
            input()
        else:
            print()
        table, adj_list = input_graph()
        while True:
            l = input().rstrip()
            if l == '':
                break
            s, d = l.split()
            print(s, d, shortest_path_distance(adj_list, table[s], table[d]))
