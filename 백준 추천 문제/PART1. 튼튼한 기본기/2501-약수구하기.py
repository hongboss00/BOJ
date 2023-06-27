# inputs
N, K = map(int, input().split())

measures = []

for m in range(1, N+1):
    if N%m == 0:
        measures.append(m)
result =  0 if (len(measures) < K) else measures[K-1]

print(result)