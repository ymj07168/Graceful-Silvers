# 음료수 얼려 먹기
import sys

# 행과 열 입력, N: 행, M: 열
N, M = map(int, sys.stdin.readline().split())

# 얼음 틀
tool = []

# 얼음 틀 모양 입력
for i in range(N):
    row = []
    inputVal = sys.stdin.readline()
    for j in range(M):
        row.append(int(inputVal[j]))
    tool.append(row)


# dfs => 얼음 구멍 탐색
def dfs(tool, s, visited):
    # 동 북 남 서
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    r = s[0]
    c = s[1]
    visited[r][c] = True    # 방문 표시
    for d in range(4):      # 동 서 남 북 위치에 탐색할 곳 있는지 확인
        rb = r + dx[d]
        cb = c + dy[d]
        if 0 <= rb and rb < N and 0 <= cb and cb < M:           # 탐색할 위치가 맵 내부 위치인지
            if tool[rb][cb] != 1 and visited[rb][cb] == False:  # 탐색할 위치가 1이 아니면서 방문한 곳이 아닌지
                s = [rb, cb]
                dfs(tool, s, visited)                           # 탐색할 위치 기준으로 다시 dfs 탐색
    return visited


# visited = [[0] * M] * N

# 얼음 구멍 개수
cnt = 0

# 방문 여부 표시 4*5
visited = [[0 for i in range(M)] for j in range(N)]

# 얼음 틀 탐색
for i in range(N):
    for j in range(M):
        start = [i, j]
        if tool[i][j] != 1 and visited[start[0]][start[1]] == False:
            cnt += 1
            visited = dfs(tool, start, visited)

print(cnt)


