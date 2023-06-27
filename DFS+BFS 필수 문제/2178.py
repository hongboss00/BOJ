import sys
from collections import deque

delta = [(0,-1), (0, 1), (-1, 0), (1, 0)]

graph = []
deq = deque()
N = 0
M = 0

def bfs(v):
    deq.append(v)

    while deq:
        _v = deq.popleft()
        (_r,_c) = _v
        for d in delta:
            (__r, __c) = tuple(sum(e) for e in zip(_v, d))
            #print(__r,__c)
            if 0 <= __r < N and 0 <= __c < M and graph[__r][__c] == 1:
                graph[__r][__c] = graph[_r][_c] + 1
                deq.append((__r, __c))

def  solution():
    bfs((0,0))
    return graph[N-1][M-1]

N,M = map(int, sys.stdin.readline().split())

for n in range(N):
    tmp = input()
    graph.append([int(e) for e in tmp])

print(solution())
