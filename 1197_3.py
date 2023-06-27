import sys
import heapq

graph = []
INF = sys.maxsize
min_v = -1
min_weight = INF

# v는 시작정점
def prim(v):
    # distance list. -> 트리를 만들어가면서 계속 D를 업데이트 해간다
    D = []
    visited = [False for _ in range(V+1)]
    mst_cost = 0

    # 입력받은 v를 시작 정점 S로하여 시작
    # S로부터 시작하기 위해 S를 heap에 넣음(weight는 0으로 하여
    # mst_cost에 영향이 없도록 한다.)
    S = v
    heapq.heappush(D, (0, S))
    '''
        방문 안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
         = 현재 만들어진 트리의 간선에 대해 최소 distance인 간선을 선택
    '''
    for k in range(1, V+1):
        # m = min_vertex
        m = -1
        min_wt = INF

        while D:
            min_wt, m = heapq.heappop(D)
            if not visited[m]:
                break
        visited[m] = True
        mst_cost += min_wt

        '''
            경로를 갱신 하는 코드 - weight update
            트리에 m vertex를 추가했으니 m으로부터 갈 수 있는 간선을 update
        '''
        for u, wt in graph[m]:
            if not visited[u] and wt < INF:
                heapq.heappush(D, (wt, u))
    return mst_cost

# Get Mst and cost of mst
def solution(v):
    return prim(v)

# inputs
V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]

for e in range(E):
    # vertex1, vertex2, weight
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

    if c < min_weight:
        min_weight = c
        min_v = a

print(solution(min_v))