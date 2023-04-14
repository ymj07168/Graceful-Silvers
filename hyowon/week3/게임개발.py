# 4-4 개임개발
import sys

# 세로, 가로 크기
N, M = map(int, sys.stdin.readline().split())

# 현재 좌표: A, B / 바라보는 방향: d(0,1,2,3)
global A, B, d
A, B, d = map(int, sys.stdin.readline().split())

# 맵 그리기 (외곽은 전체 바다 1, 육지 0)
app_map = []
for i in range(N):
    column = list(map(int, sys.stdin.readline().split()))
    app_map.append(column)


# 방향 설정 (북, 동, 남, 서)
dir_list = [[(-1, 0), (0, 1), (1, 0), (0, -1)],
            [(0, 1), (1, 0), (0, -1), (-1, 0)],
            [(1, 0), (0, -1), (-1, 0), (0, 1)],
            [(0, -1), (-1, 0), (0, 1), (1, 0)]]


# 움직인 횟수
global cnt
cnt = 1

# 처음 시작 좌표 방문 표시
app_map[B][A] = 1

# 한 칸씩 좌표 움직이고 방향 설정하는 함수
def setDir(dir):
    global A, B, d, cnt
    for x, y in dir_list[d]:
        if ((0 <= A + x) and (A + x <= M)) and ((0 <= B + y) and (B + y <= N)):
            if app_map[B+y][A+x] != 1:
                app_map[B+y][A+x] = 1
                A = A+x
                B = B+y
                cnt += 1
                if x == 0 and y == -1:
                    d = 0
                    return 0
                elif x == 1 and y == 0:
                    d = 1
                    return 0
                elif x == 0 and y == 1:
                    d = 2
                    return 0
                elif x == -1 and y == 0:
                    d = 3
                    return 0
    return -1

while True:
    dir = setDir(d)
    if dir == -1:
        break

print(cnt)




