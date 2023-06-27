import sys
import math
from collections import deque

T = int(input())
cases = deque()

for _ in range(T):
    cases.append(tuple(map(int, sys.stdin.readline().split(' '))))


# 1. r1 + r2 < distance -> 0
# 2. r1 + r2 = distance -> 1
# 3. r1 + r2 = distance -> case     따져봐야함
# 3.1.  distance - min < max < distance + min -> 2개
# 3.2.  max < distance + min -> 1 or -1
# 3.3.  max > distance + min -> 0
for x1, y1, r1, x2, y2, r2 in cases:
    distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    m = min(r1, r2)
    M = max(r1, r2)
    r = r1 + r2

    # 무한대 case 분리
    if r1 == r2 and distance == 0:
        print(-1)
        continue

    if r < distance:
        print(0)
    elif r == distance:
        print(1)
    else:
        if distance - m < M and distance + m > M :
            print(2)
        elif M == distance + m:
            print(1)
        elif M > distance + m:
            print(0)
