import sys
from collections import deque

graph = deque()
min_weight = 0
min_edge = 0

def kruskal():
    #임의의 vertex u와v
    def union(u,v):
        root1 = find(u)
        root2 = find(v)
        # 임의로 root2의 부모 vertex를 root1로 바꿈으로써(바뀌어도 상관없다)
        # 같은 tree로 만들어 버림.
        p[root2] = root1
        return

    # 경로 압축 / 부모 vertex 최신화
    def find(v):
        if v != p[v]:
            p[v] = find(p[v])
        return p[v]

    # 각 vertex의 부모 vertex를 나타내는 list p의 초기화
    # 초기에는 자기 자신이 부모 vertex가 된다.
    p = []
    for i in range(V):
        p.append(i)

    mst_cost = 0
    # 간선의 갯수 만큼 반복
    for e in range(E):
        u, v, w = graph.popleft()
        if find(u) != find(v):
            union(u, v)
            mst_cost += w

    return mst_cost

# Get Mst and cost of mst
def solution(l):
    # 일단 weight의 크기 순으로 정렬(내림차순)
    l.sort(key = lambda x:x[2])
    graph.extend(l)
    return kruskal()

# inputs
V, E = map(int, input().split())

tmp = []
for e in range(E):
    # vertex1, vertex2, weight
    a, b, c = map(int, sys.stdin.readline().split())

    if c < min_weight:
        min_weight = c
        min_vertex = a

    tmp.append((a-1,b-1,c))

print(solution(tmp))