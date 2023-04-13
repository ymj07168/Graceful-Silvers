# N x M
#N, M = map(int, input().split())
# x, y 좌표 및 0 북 / 1 동 / 2 남 / 3 서
#A, B, d = map(int, input().split())
# 맵 외곽 바다
#map_list = []
#for i in range(N):
#    map_list.append(list(map(int, input().split())))
#print(map_list)

# 반시계 90도 회전 방향
#new_d = [(0, -1), (-1, 0), (0, 1), (1, 0)]

#while True:
    # 캐릭터 왼쪽 new_d 방향 가지 않은 곳 존재시
#    if A + new_d[0] >=0 and A + new_d[0] <= N-1 and B + new_d[1] >=0 and B + new_d[1] <=M-1:

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x, y, 방향 입력
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북동남서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def trun_left():
    # 0 ~ 3을 유지함
    global direction
    direction -=1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽 회전
    trun_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸 존재 => 이동
    if d[nx][ny] == 0 and array[x][y] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        trun_time = 0
        continue
    # 회전한 이후 정면 가보지 않은 칸 없거나 바다
    else:
        turn_time +=1
    # 네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤 바다 막힌 경우
        else:
            break
        turn_time = 0

print(count)
