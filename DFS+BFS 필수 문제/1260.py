# Vertex는 1부터 존재 -> index 고려하기 참 머리아프네

# N - number of Vertex
# M - number of Edge
# V - entrypoint vertex
N = 0
M = 0
V = 0

isVisited = []
weight = []

def dfs(vertex):
    isVisited[vertex] = True
    print(vertex, end =' ')

    # w -> weight에서 v행
    for n in range(1, N+1):
        if weight[vertex][n] == 1 and not isVisited[n]:
            dfs(n)
    return

def bfs(vertex):
    isVisited[vertex] = True
    queue = []

    queue.append(vertex)
    while len(queue):
        v = queue.pop(0)
        print(v, end=' ')

        for n in range(1, N+1):
            if weight[v][n] == 1 and not isVisited[n]:
                isVisited[n] = True
                queue.append(n)
    return

##########################################################################################
# Input
# 첫 줄 입력
N, M, V = map(int, input().split())

# 행렬로 구현
weight = [[0] * (N+1) for _ in range(N+1)]
isVisited = [False for _ in range(N+1)]

# M개의 입력 - edge 완성
for k in range(M):
    i, j = map(int, input().split())
    weight[i][j] = weight[j][i] = 1

##########################################################################################
# OutPut
# DFS 수행
dfs(V)

isVisited = [False for _ in range(N+1)]
print()

# BFS 수행
bfs(V)