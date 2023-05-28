# 미래 도시
# 다익스트라 알고리즘 해설

import heapq
INF = int(1e9)

n, m = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]

# 모든 간선 정보를 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  # 양방향 그래프이므로 a번 노드 <-> b번 노드 이동 비용이 1라는 의미
  graph[a].append((b, 1))
  graph[b].append((a, 1))

# 물건 판매를 위해 방문할 x 회사, 소개팅 상대가 있는 k 회사를 입력받음
x, k = map(int, input().split())
  
def dijkstra(start):
  
  q = []
  
  # 최단 거리 테이블을 모두 무한으로 초기화
  distance = [INF] * (n + 1)

  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:  # 큐가 비어있지 않다면
    dist, now = heapq.heappop(q)  # now 노드까지 가는 최단거리가 dist
    
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[now] < dist:
      continue
    
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  
  return distance
        
# 다익스트라 알고리즘을 수행
d1k = dijkstra(1)[k]  # 1회사 -> k회사
dkx = dijkstra(k)[x]  # k회사 -> x회사

d1x = d1k + dkx   # 1번 회사에서 출발하여 k번 회사를 거쳐 x번 회사로 가는 최소 이동 시간

if d1x >= INF:
  print(-1)
else:
  print(d1x)