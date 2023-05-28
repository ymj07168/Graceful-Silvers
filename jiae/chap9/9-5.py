# 전보

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수, 시작 노드를 입력 받기
n, m, c = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
  x, y, z = map(int, input().split())
  # x번 노드 -> y번 노드 이동 비용이 z라는 의미
  graph[x].append((y, z)) 

def dijkstra(start):
  
  q = []

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
dijkstra(c)

count = 0  # 도달할 수 있는 노드의 개수
max_time = 0   # 모든 도시들이 메시지를 받는 데 걸리는 시간

for d in distance:
  if d ==0 or d == INF:  # 시작 노드와 도달할 수 없는 노드는 제외
    continue
  else:
    count += 1
    max_time = max(max_time, d)

print(count, max_time)