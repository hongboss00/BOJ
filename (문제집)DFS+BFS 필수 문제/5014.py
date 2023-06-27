import sys
from collections import deque

deq = deque()

def bfs(v):
    deq.append(v)
    visited[v] = True
    while deq:
        _v = deq.popleft()

        if _v == G:
            return count[G]

        for i in (_v + U, _v - D):
            if 0 <= i < F and not visited[i]:
                deq.append(i)
                visited[i] = True
                count[i] = count[_v] + 1

    return 'use the stairs'

def solution():
    return bfs(S)


F,S,G,U,D = map(int, input().split())
direction = False if S-G < 0 else True

S -= 1
G -= 1
visited = [False for _ in range(F)]
count = [0 for _ in range(F)]


# Up 방향 간선

# Down 방향 간선

print(solution())