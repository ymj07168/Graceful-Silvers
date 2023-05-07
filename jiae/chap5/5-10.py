# 음료수 얼려먹기

N, M = map(int, input().split())

icetray = []
for _ in range(N):
  icetray.append(list(map(int, input())))
  
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(graph, x, y):
  
  graph[y][x] = 2   # 해당 좌표 방문 표시
  
  for i in range(4):  # 상하좌우 좌표 확인
    
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx < 0 or nx >= M or ny < 0 or ny >= N:  # 좌표가 범위 밖이면 다음 방향 탐색
      continue
    
    if graph[ny][nx] == 1 or graph[ny][nx] == 2: # 막혀있거나 이미 방문한 좌표면 다음 방향 탐색
      continue
    
    if graph[ny][nx] == 0:  # 방문하지 않은 좌표면 재귀적으로 dfs 함수 호출
      dfs(graph, nx, ny)
      
icecream = 0
for x in range(M):
  for y in range(N):
    if icetray[y][x] == 0:
      dfs(icetray, x, y)
      icecream += 1

print(icecream)