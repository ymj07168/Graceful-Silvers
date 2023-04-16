# 게임 개발

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = []
for i in range(n):
  d.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]

d[x][y] = 2   # 현재 좌표 방문 처리
visited = 1   # 이동한 칸 수 증가

while True:
  for q in range(4):
    # 방문 예정 좌표 계산
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 왼쪽 방향으로 회전
    direction -= 1
    if direction == -1: 
      direction = 3
    
    # 맵 외곽인 경우
    if nx < 1 or ny < 1 or nx > n-1 or ny > m-1:
      continue
    
    if d[nx][ny] == 1:  # 바다여서 가지 못하는 경우
      continue
    
    if d[nx][ny] == 0:  # 방문하지 않은 칸(육지)인 경우
      d[nx][ny] = 2     # 방문 처리
      visited += 1      # 이동한 칸 수 증가
      x = nx            # 좌표값 업데이트
      y = ny
      continue
  
  # 네 방향 이미 가본 칸이거나 바다로 되어있는 칸인 경우, 한 칸 뒤로 가기
  backward = (direction + 2) % 4
  nx += dx[backward] 
  ny += dy[backward]
  
  # 한 칸 뒤로 가려할 때, 뒤쪽이 바다면 움직임을 멈춤
  if d[nx][ny] == 1:
    break
  else:
    x = nx
    y = ny
  
print(visited)