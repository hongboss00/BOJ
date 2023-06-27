graph = []
ancestors = []
n = 0

def dfs(v):
    ancestors.append(v)

    for i in range(n+1):
        if graph[v][i] == 1:
            dfs(i)

    return


# n-> 총 사람 수
n = int(input())
# 촌수를 알아내야하는 두 사람
target1, target2 = map(int, input().split())
# 부모자식 관계(edge)의 갯수
m = int(input())

graph = [[-1] * (n+1) for _ in range(n+1)]

for w in range(m):
    x, y = map(int, input().split())
    graph[y][x] = 1



##########################
# Output
dfs(target1)
ancestors1 = ancestors
ancestors = []
dfs(target2)

output = -1
for i in range(len(ancestors1)-1, -1, -1):
    for j in range(len(ancestors)):
        if ancestors1[i] == ancestors[j]:
            output = i+j

print(output)