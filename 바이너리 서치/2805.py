import sys

N, M = map(int, sys.stdin.readline().split(' '))
trees = list(map(int, sys.stdin.readline().split(' ')))
trees.sort()

left = 0
right = trees[-1]
answer = 0

while left <= right:
    mid = (left + right) // 2

    result = 0
    for i in range(N-1, -1, -1):
        if trees[i] <= mid:
            break
        result += (trees[i] - mid)

    if result < M:
        right = mid - 1

    else:
        left = mid + 1
        answer = mid

print(answer)