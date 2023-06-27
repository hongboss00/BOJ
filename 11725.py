import sys

sys.setrecursionlimit(10**6)

N = 0
isVisited = []
graph = []
parent = []


# 행렬로 구현
weight = [[0] * (N+1) for _ in range(N+1)]
isVisited = [False for _ in range(N+1)]


def dfs(vertex):
    isVisited[vertex] = True

    # w -> weight에서 v행
    for n in graph[vertex]:
        if not isVisited[n]:
            parent[n] = vertex
            dfs(n)
    return

#############################################################

N = int(input())

graph = [[] for _ in range(N+1)]
isVisited = [False for _ in range(N+1)]
# isVisited = [False] * (N+1)
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    m, n = map(int, input().split())
    graph[m].append(n)
    graph[n].append(m)

dfs(1)

for p in parent[2:]:
    print(p)


