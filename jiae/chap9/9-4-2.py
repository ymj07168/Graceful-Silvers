# 미래 도시
# 플로이드 워셜 알고리즘 해설

INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0
      
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A <-> B로 가는 비용은 1로 설정(양방향 그래프)
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 최종 목적지 노드인 x, 거쳐갈 회사인 k를 입력받음
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      
# 수행된 결과를 출력
d1x = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if d1x >= INF:
  print(-1)
# 도달할 수 있다면, 최단 거리를 출력
else:
  print(d1x)