# 미로 탈출
import sys

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


from collections import deque

def bfs(r, c, cnt):
    # 상 하 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    if r <= -1 or r >= N or c <= -1 or c >= M:
        return False
    if graph[r][c] == 1:
        rq = deque([r])           # 행값 큐 생성
        cq = deque([c])           # 열값 큐 생성

        while rq and cq:        # rq와 cq에 값이 남아 있을 때까지 탐색
            r = rq.popleft()
            c = cq.popleft()

            graph[r][c] = 2
            cnt += 1
            if r == N-1 and c == M-1:
                break

            # 상하좌우 갈 곳 있는지 없는지 체크
            no = 0
            for i in range(4):
                if 0 <= r + dx[i] and r + dx[i] < N and 0 <= c + dy[i] and c + dy[i] < M:
                    if graph[r+dx[i]][c+dy[i]] == 1:
                        rq.append(r + dx[i])
                        cq.append(c + dy[i])
                    else:
                        no += 1
                else:
                    no += 1

            # 상하좌우 갈 곳 없을때 back => cnt 빼기
            if no == 4:
                cnt -= 1


    return cnt

# 이동한 칸 개수
cnt = 0

cnt = bfs(0, 0, cnt)

print(cnt)

