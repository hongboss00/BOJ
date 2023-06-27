from collections import deque
graph = []
visited = []

def bfs(vertex):
    q = deque()
    infected = 0

    visited[vertex] = True
    q.append(vertex)
    while(q):
        v = q.popleft()
        infected = infected + 1
        for i in range(N+1):
            if graph[v][i] == 1 and visited[i] == False:
                q.append(i)
                visited[i] = True
    return infected - 1

#############################################
#input
N = int(input())
E = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(E):
    i,j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1
#############################################
#output

print(bfs(1))