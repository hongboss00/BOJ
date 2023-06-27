import sys

N, M = 0, 0
dirty = 0
clean = 0
room = []

class robot():
    def __init__(self, r, c, d, m):
        self.r = r
        self.c = c
        self.d = d
        self.room = m
        self.num_cleaning = 0

    def location(self):
        return (self.r, self.c)

    def rotate(self):
        #왼쪽 방향으로 1번 회전한다.
        self.d = (self.d + 3) % 4

    def move_forward(self):
        if self.d % 2 == 0:
            self.r = self.r - 1 + self.d
        else:
            self.c = self.c + 2 - self.d
        return

    def move_backward(self):
        if self.d % 2 == 0:
            self.r = self.r + 1 - self.d
        else:
            self.c = self.c - 2 + self.d
        return

    def find_next(self):
        if self.d % 2 == 0:
            return (self.r, self.c - 1 + self.d)
        else:
            return (self.r - 2 + self.d, self.c)

        return (-1, -1)

    def find_backward(self):
        if self.d % 2 == 0:
            return (self.r + 1 - self.d, self.c)
        else:
            return (self.r, self.c -2 + self.d)

def solution(robot):
    count = 0

    while True:
        # 청소할 수 있는 최대 범위를 넘어버리면 탈출
        if count >= dirty:
            return count

        (r,c) = robot.location()
        if room[r][c] == 0:
            room[r][c] = -1
            count += 1

        i = 0
        while i < 4:
            (_r, _c) = robot.find_next()
            status = room[_r][_c]

            if status == 0:
                robot.rotate()
                robot.move_forward()

                room[_r][_c] = -1
                count += 1
                i = 0

            else:
                robot.rotate()
                i = i + 1

        (__r, __c) = robot.find_backward()
        status = room[__r][__c]

        if status == 1:
            break
        else:
            robot.move_backward()
            continue

    return count

# input
# N : row개수
# M : column개수
N, M = map(int, input().split())
init_r,init_c,init_d = map(int, input().split())

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    room.append(tmp)

dirty = N * M - sum(sum(l) for l in room)
#print(dirty)

#output
r = robot(init_r, init_c , init_d, room)
print(solution(r))

'''
for i in range(N):
    for j in range(M):
        print('%s'%(room[i][j]), end = ' ')
    print()
'''