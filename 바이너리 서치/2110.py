import sys

N, C = map(int, sys.stdin.readline().split(" "))
X = list()

for i in range(N):
    X.append(int(sys.stdin.readline()))

X.sort()

# 목표 -> 가능한 거리에 대해서 최댓값을 찾아낸다
# 거리에 대해 이진탐색을 실시
# 1. 최소 거리를 1로하고, 최대 거리를 마지막 집 - 첫 집 으로 한다.
# 2. 거리를 기준으로 이진 탐색을 하여 mid값으로 설치할 시 만족하는 지 확인
#    mid값이 당시의 최선의 최댓값이 것.
# 4. 위를 만족하는 거리 중 최댓값을 출력! -> 최댓값!!
left = 1
right = X[-1] - X[0]
answer = 0

while left <= right:
    mid = (left+right)//2

    # 시작은 첫 집을 기준으로
    pre = X[0]
    installed = 1

    for i in range(len(X)):
        if X[i] - pre >= mid:
            installed += 1
            # 거리의 최댓값을 찾아서 이동
            pre = X[i]

    # 설치된게 부족하다면 거리를 줄여서 실시
    if installed < C:
        right = mid - 1
    # 설치된게 더 많다면 거리를 더 늘려서 실시
    elif installed > C:
        left = mid + 1
        answer = max(answer, mid)
    # 딱 맞게 떨어지면 거리를 하나 더 늘려봄
    else :
        left = mid + 1
        answer = mid

print(answer)