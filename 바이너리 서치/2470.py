import sys

N = int(sys.stdin.readline())
vals = sorted(list(map(int, sys.stdin.readline().split(' '))))

# 1. 입력 value들을 일단 정렬
# 2. 왼쪽에서 가는 left값, 오른쪽에서 가는 right값
# 3. left + right 해서 minimum보다 작으면 min업데이트 및 left 증가
# 4. minumum보다 크면은 right 감소

left = vals[0]
right = vals[-1]

# 일단 무한대 -> 그냥 문제 조건에서 주어진 범위를 참고하여서 설정
answer = (0,0)
min = int(1e10)


while left <= right :
    summation = abs(left + right)
    if summation < min:
        min = summation
        answer = (left, right)
        left += 1

    else :
