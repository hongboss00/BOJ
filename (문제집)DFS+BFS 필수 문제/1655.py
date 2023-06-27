import heapq as hq
import sys
from collections import deque

l_heap = []
r_heap = []

lN = 0
rN = 0

lPeek = -sys.maxsize
rPeek = sys.maxsize

answer = deque()

M = int(sys.stdin.readline())

for m in range(M):
    a = int(sys.stdin.readline())

    if lN > rN:
        if a < lPeek:
            hq.heappush(l_heap, (-a, a))
            t = hq.heappop(l_heap)[1]
            hq.heappush(r_heap, (t,t))
        else:
            hq.heappush(r_heap, (a,a))
        rN += 1

    else:
        if rPeek <= a:
            hq.heappush(r_heap, (a, a))
            t = hq.heappop(r_heap)[1]
            hq.heappush(l_heap, (-t,t))
        else:
            hq.heappush(l_heap, (-a,a))
        lN += 1
    if l_heap:
        lPeek = l_heap[0][1]
    if r_heap:
        rPeek = r_heap[0][1]

    answer.append(lPeek)

while answer:
    print(answer.popleft())