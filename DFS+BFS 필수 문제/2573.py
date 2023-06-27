import sys
from collections import deque
mountains = []
# left right top bottom
delta = [(0,-1), (0,1), (-1,0), (1,0)]

deq = deque()
p_deq = deque()
m_deq = deque()

def printmountaints():
    for i in range(N):
        print(*mountains[i])
    print()

# 빙산을 녹이기
def melting(q):
    while q:
        (r,c,i) = q.popleft()
        a = mountains[r][c] - i
        if a <= 0:
            mountains[r][c] = 0
        else:
            mountains[r][c] = a
            p_deq.append((r,c))
    return

# bfs실행
def bfs(v, visited):
    global deq

    (r,c) = v
    visited[r][c] = True
    deq.append(v)
    while deq:
        _v = deq.popleft()
        _r,_c = _v
        #print(_v)
        cnt = 0
        for d in delta:
            __v = (__r,__c) = tuple(sum(e) for e in zip(_v,d))
            if 0 <= __r < N and 0 <= __c < M :
                if mountains[__r][__c] > 0 and not visited[__r][__c]:
                    deq.append(__v)
                    visited[__r][__c] = True
                elif mountains[__r][__c] == 0:
                    cnt += 1
        m_deq.append((_r, _c, cnt))
    #print()

def solution():
    global tmp

    year = 0
    while True:
        visited = [[False] * M for _ in range(N)]
        # bfs를 시행 하여 연결성분의 갯수 확인
        #print(visited)
        cnt = 0
        while p_deq:
            v = p_deq.popleft()
            r,c = v
            if not visited[r][c]:
                bfs((r,c), visited)
                cnt += 1
                if cnt >= 2:
                    return year

        if cnt == 0:
            return 0

        # Melting O(N**2)
        melting(m_deq)

        #printmountaints()
        year += 1
    return 0


N, M = map(int, sys.stdin.readline().split())
visited = [[False] * M for _ in range(N)]

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if tmp[j] != 0:
            p_deq.append((i,j))
    mountains.append(tmp)

print(solution())