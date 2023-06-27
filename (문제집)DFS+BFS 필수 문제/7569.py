'''
    Runtime Error
    1. queue를 사용
    2. len함수의
        - 리스트의 길이를 알기 위해 혹은 마지막 인덱스를 알기 위해 len을 자주 쓰는데 이놈이 은근히

'''
import sys
from collections import deque
# BFS를 위한 deque
# -> queue를 사용하지 않는 이유 queue의 pop연산은 선형시간인데 비해 deque는 상수시간이다
deq = deque()
tomatoes = []

# 0,1 -> left, right
# 2,3 -> front, behind
# 4,5 -> top, bottom
#dx = [-1,1,0,0,0,0]
#dy = [0,0,1,-1,0,0]
#dz = [0,0,0,0,1,-1]
delta = [(0,0,1), (0,0,-1),
         (-1,0,0), (1,0,0),
         (0,1,0), (0,-1,0)]

def solution():
    z, x, y = 0,0,0
    day = 0
    # 일단 토마토 다 숙성시킴
    while(deq):
        z, x, y = deq.popleft()

        for dz, dx, dy in delta:
            _z = z + dz
            _x = x + dx
            _y = y + dy
            if 0 <= _z < H and 0 <= _x < N and 0 <= _y < M and tomatoes[_z][_x][_y] == 0:
                ripness = tomatoes[z][x][y] + 1
                tomatoes[_z][_x][_y] = ripness
                day = max(day, ripness)
                deq.append((_z,_x,_y))

    for h in tomatoes:
        for n in h:
            for m in n:
                if m == 0:
                    return -1

    return day - 1 if day > 0 else day

#############################################
#input
# M : 가로 크기(columns)
# N : 세로 크기(rows)
# H : 높이(height)
M, N, H = map(int, input().split())

for h in range(H):
    tmp = []
    for n in range(N):
        # 1 X M 사이즈의 list 를 N번 쌓아 N X M 행렬 1개 층 생성
        # input이 좀 많아서 runtime error 방지를 위해 sys.stdlin 입력 사용
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for m in range(M):
            if tmp[n][m] == 1:
                deq.append((h,n,m))
    tomatoes.append(tmp)
#############################################
#output

# 토마토 숙성시키기
print(solution())