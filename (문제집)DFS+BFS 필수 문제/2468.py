import sys
from collections import deque
# N의 최대 값이 100 이므로 recursion 최댓값 설정
# 각 높이는 1이상임이 보장
sys.setrecursionlimit(1000000)

visited = []
deq = deque()
delta = [(0,-1), (0,1), (-1,0), (1,0)]

graph = []
min_height = 0
max_height = 0

# e: visited
def dfs(v, h):
    global visited

    (r,c) = v
    visited[r][c] = True

    for d in delta:
        (_r,_c) = tuple(sum(e) for e in zip(v,d))
        if 0 <= _r < N and 0 <= _c < N and not visited[_r][_c] and graph[_r][_c] > h:
            dfs((_r, _c), h)
    return

def bfs(v, h):
    global visited
    global deq

    (r,c) = v
    visited[r][c] = True
    deq.append(v)

    while deq:
        _v = deq.popleft()
        for d in delta:
            __v = (__r,__c) = tuple(sum(e) for e in zip(_v,d))
            if 0 <= __r < N and 0 <= __c < N and not visited[__r][__c] and graph[__r][__c] > h:
                deq.append(__v)
                visited[__r][__c] = True

def solution():
    global visited

    # 각 높이가 1이상인것이 보장되므로
    if max_height ==1:
        return 1

    # 각 케이스에 대해 연결성분의 갯수 리스트로 저장
    cnt_components = []

    for h in range(max_height):
        visited = [[False] * N for _ in range(N)]
        cnt = 0

        for i in range(N):
            for j in range(N):
                if not visited[i][j] and graph[i][j] > h:
                    dfs((i,j),h)
                    cnt += 1

        cnt_components.append(cnt)
    #print(cnt_components)
    return max(cnt_components)

N, M = map(int, input().split())
visited = [[False] * N for _ in range(N)]

for n in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    min_height = min(min_height, min(tmp))
    max_height = max(max_height, max(tmp))
    graph.append(tmp)

print(solution())