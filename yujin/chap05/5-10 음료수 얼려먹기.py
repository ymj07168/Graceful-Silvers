# 뭉텅이로 나오게 DFS
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
 # DFS로 특정한 노드 방문한 뒤 연결된 모든 노드 방문
def dfs(x, y):
    # 종료조건
    if x <=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재노드 방문x면
    if graph[x][y] ==0:
        # 방문처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
        dfs(x -1, y)
        dfs(x, y -1)
        dfs(x +1 , y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현위치 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)