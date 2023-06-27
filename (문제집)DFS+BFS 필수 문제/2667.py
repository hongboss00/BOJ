import sys
from collections import deque

map = []
visited = []

delta = [(0,-1), (0,1), (-1,0), (1,0)]

def bfs(location):
    count = 0
    deq = deque()
    deq.append(location)
    visited[location[0]][location[1]] = True

    while(deq):
        pos = deq.popleft()
        count = count + 1
        for d in delta:
            _pos = tuple(sum(elements) for elements in zip(pos, d))
            r = _pos[0]
            c = _pos[1]

            if 0 <= r < N and 0 <= c < N and not visited[r][c] and map[r][c] == 1:
                deq.append(_pos)
                visited[r][c] = True

    return count

def solution():
    result = []
    for i in range(N):
        for j in range(N):
            if map[i][j] == 1 and not visited[i][j]:

                result.append(bfs((i, j)))
    result.sort()
    return result

# input
N = int(sys.stdin.readline())

visited = [[False] * N for _ in range(N)]

for i in range(N):
    tmp = list(input())
    map.append([int(e) for e in tmp])

#output
result = solution()
print(len(result))
for i in result:
    print(i)