import sys
from collections import deque

MAX_N = 100000

result = [0 for _ in range(MAX_N+1)]
result[1] = 1

def find(i):
    num = i
    while (num != 1) and (num != 0):
        num = result[num]
    return num

N = int(input())

for _ in range(N-1):
    n, m = map(int, sys.stdin.readline().split(' '))

    if find(n) == 1:
        result[result[m]] = m
        result[m] = n
    elif find(m) == 1:
        result[n] = m
    else:
         result[m] = n




for i in range(2, N+1):
    print(result[i])

print(result[2:N+1])