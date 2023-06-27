N = int(input())
A = list(map(int, input().split()))

M = int(input())
X = list(map(int, input().split()))

A.sort()

for x in X:
    start = 0
    end = N-1
    mid = int((start + end)/2)
    isin = False

    while start <= end:
        mid = int((start + end) / 2)
        a = A[mid]

        if a == x:
            isin = True
            break
        elif a > x:
            end = mid-1
        elif a < x:
            start = mid+1

    if isin:
        print("1")
    else:
        print("0")
