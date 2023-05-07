from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()
        # 현위치에서 네방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx <0 or ny<0 or nx>=n or ny>=m:
                continue
            # 벽 무시
            if graph[nx][ny] ==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx, ny))
        # 가장 오른쪽 아래까지 최단 거리 반환
        return graph[n-1][m-1]
print(bfs(0,0))

# 뭐징 이거 1나옴
#5 6
#101010
#111111
#000001
#111111
#111111