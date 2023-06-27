import sys

locations = []
graph = []
visited = []

def distance(p1, p2):
    return sum(abs(e[0] - e[1]) for e in zip(p1,p2))

# t: Test Case, v: Vertex, l : 결과를 저장할 list
def dfs(t,v,l):
    if v == N[t]+1:
        l[t] = True
    visited[t][v] = visited
    for i in range(N[t]+2):
        if graph[t][v][i] and not visited[t][i]:
            dfs(t, i, l)
    return

def solution():
    results = [False for _ in range(T)]
    for t in range(T):
        # 간선 만들기!
        for i in range(N[t]+2):
            for j in range(i, N[t]+2):
                if distance(locations[t][i], locations[t][j]) <= 1000:
                    graph[t][i][j] = graph[t][j][i] = 1
        #dfs 실행 및 결과 resuls에 저장
        dfs(t, 0, results)

    return results

# 테스트 케이스의 개수
T = int(sys.stdin.readline())
locations = [[] for _ in range(T)]
N = [0 for _ in range(T)]
# input
for t in range(T):
    # 편의점의 개수
    N[t] = int(sys.stdin.readline())

    # graph / visited 생성
    graph.append([[0] * (N[t]+2) for _ in range(N[t]+2)])
    visited.append([False for _ in range(N[t]+2)])

    # 상근이네 좌표
    x,y = map(int, sys.stdin.readline().split())
    locations[t].append((x,y))
    # 페스티벌 좌표
    _x,_y = map(int, sys.stdin.readline().split())
    locations[t].append((_x,_y))

    # 편의점의 좌표들
    for n in range(N[t]):
        __x, __y = map(int, sys.stdin.readline().split())
        locations[t].append((__x, __y))

#output
result = solution()
for r in result:
   if r:
       print('happy')
   else:
       print('sad')