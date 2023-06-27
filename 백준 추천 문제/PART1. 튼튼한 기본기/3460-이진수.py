import sys

T = int(input())
N = list()

for _ in range(T):
    N.append(int(sys.stdin.readline()))

for n in N:
    results = list()
    t = n
    while t != 1:
        results.append(t%2)
        t= t//2
    results.append(1)

    for i in range(len(results)):
        if results[i]:
            print(i, end=' ')