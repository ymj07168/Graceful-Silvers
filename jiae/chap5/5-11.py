# 미로 탈출
# BFS를 이용하면 효과적으로 해결할 수 있다(BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프르이 모든 노드를 탐색하기 때문!)

from collections import deque

N = 5
M = 6

graph = []
for _ in range(N):
  graph.append(list(map(int, input())))
  
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, x, y):
  que = deque()
  que.append((x, y))
  
  while que:
    x, y = que.popleft()

    for i in range(4):  # 현재 위치에서 네 방향으로의 위치 확인
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 좌표가 범위 밖이면 다음 방향 탐색
        continue
      
      if graph[nx][ny] == 0:  # 벽인 경우 무시
        continue
      
      if graph[nx][ny] == 1:  # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        graph[nx][ny] = graph[x][y] + 1
        que.append((nx, ny))
        
  return graph[N-1][M-1]
  
print(bfs(graph, 0, 0))