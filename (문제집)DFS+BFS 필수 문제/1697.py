import sys
from collections import deque

deq = deque()

def bfs(v):
    deq.append(v)
    visited[v] = True
    while deq:
        _v = deq.popleft()

        if _v == K:
            return count[K]

        for i in (_v -1, _v + 1, 2*_v):
            if 0 <= i <= M and not visited[i]:
                deq.append(i)
                visited[i] = True
                count[i] = count[_v] + 1

    return 0

def solution():
    return bfs(N)

M = 100000
N, K = map(int, input().split())

visited = [False for _ in range(M+1)]
count = [0 for _ in range(M+1)]

print(solution())