x, y, W, S = map(int, input().split(' '))

def solution():
    # 1. 최솟값 좌표만큼 대각선으로 이동
    # 2. 남은게 짝수 -> 남은 만큼 대각선 이동
    # 3. 남은개 홀수 -> (남은거 - 1)만큼 대각선 + 한 개의 십자이동
    m = min(x, y)
    M = max(x, y)

    last = M - m
    if S < W :
        # 남은게 짝수
        if last % 2 == 0:
            return (m + last) * S
        else:
            return (last+m-1)*S + W


    if S > 2*W:
        return (x + y) * W
    else:
        return m * S + last * W

print(solution())