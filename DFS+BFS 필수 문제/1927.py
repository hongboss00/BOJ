import sys
from collections import deque

# 리스트로 구현하는 이진 힙
class BHeap:
    def __init__(self):
        self.l = [None]
        self.N = 0

    '''
    def __init__(self, l):
        self.l = l
        self.N = len(l) - 1
    '''
    def create_heap(self):          # 초기 힙 생성
        # i는 이파리 노드 이전의 노드들에 대해 시행
        for i in range(self.N//2 ,0, -1):
            self.downheap(i)

    def print_heap(self):
        while self.N > 0:
            print(self.pop(), end = '')

    # l[0]은 사용치 않는다. 그냥 그게 편행
    def pop(self):
        if self.N == 0:
            return None

        # pop 되어야할 대상 일단 저장
        min = self.l[1]
        # 마지막 노드와 첫 노드를 교환
        self.l[1], self.l[-1] = self.l[-1], self.l[1]
        # 마지막 노드가 되어진 pop대상을 삭제 및 리스트 크기 감소
        del self.l[-1]
        self.N -= 1
        # 새로 바뀌게 된 첫 노드에 대해  downheap을 실시하여 규칙 유지
        self.downheap(1)

        return min

    def push(self, a):
        self.N += 1
        self.l.append(a)

        self.upheap(self.N)

    # dwonheap 과 upheap은 Recursion으로 구현해도 좋다.
    def downheap(self, i):
        while 2 * i <= self.N:
            # k는 i의 자식노드 중 왼쪽꺼
            k = 2 * i
            # 자식 노드 둘 중 더 작은 놈을 비교대상으로한다.
            if k < self.N and self.l[k] > self.l[k+1]:
                k += 1

            # 규칙을 만족하게 되면 탈출
            if self.l[i] < self.l[k]:
                break

            self.l[i], self.l[k] = self.l[k], self.l[i]
            i = k
        return

    def upheap(self, j):
        while j > 1 and self.l[j//2] > self.l[j]:
            self.l[j], self.l[j//2] = self.l[j//2], self.l[j]
            j = j // 2

        return

# sol
def solution():
    global h

    while deq:
        a = deq.popleft()

        if a == 0:
            b = h.pop()
            b = 0 if b == None else b
            print(b)
        else:
            h.push(a)

deq = deque()

# 1<=N <= 10**5
N = int(input())
h = BHeap()

for n in range(N):
    t = int(sys.stdin.readline().split()[0])
    '''
    if t == 0:
        j = h.pop()
        j = 0 if j == None else j
        print(j)
    else:
        h.push(t)
    '''
    deq.append(t)

solution()


print(l_heap[0][1] if medium == INF else medium)
print(l_heap, end=' ')
print(medium, end = ' ')
print(r_heap)
print()