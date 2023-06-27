import sys
sys.setrecursionlimit(10**5)

def solution(n, r, c):
    if n == 1:
        return (r*2 + 1) + c

    half = 2**(n-1)
    m = ((r//half) * 2 + 1) + (c//half)

    _r, _c = r % half, c % half

    return (m-1)*((half)**2) + solution(n-1, _r, _c)

N, r, c = map(int, input().split())

print(solution(N, r, c ) - 1)