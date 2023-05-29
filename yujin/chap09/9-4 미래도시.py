INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력 받기
n, m = map(int,input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
# 최단 거리 구하는 것이므로 무한으로 싹 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b  in range(1, n+1):
        if a == b:
            # 자기 => 자기
            graph[a][b] = 0
            # 인덱스를 a -> b로 가는 것으로 생각하고 저장

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for i in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정(각 간선 양방향 비용 1)
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 여기까지 오게 되면 노드와 간선별로 그래프가 그려진다.
# graph의 인덱스로 접근했을 때 노드가 없는 간선에 대한 길은 전부 무한으로 표시되게 된다.

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기 => ? 책 오타? k 경유이고 x가 최종인데
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # k가 경유하는 곳
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
# 도달할 수 있으면 최단거리 출력
else:
    print(distance)