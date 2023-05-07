//
// Created by 김민지 on 2023/05/01.
//
#include "iostream"
#include "queue"

using namespace std;

int n, m;
int graph[201][201];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int bfs(int x, int y) {
    queue<pair<int, int>> q;
    q.push({x, y});
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (!graph[nx][ny]) continue;   // 괴물(벽)인 경우
            if (graph[nx][ny] == 1) {       // 해당 노드를 처음 방문하는 경우에만 최단거리 기록
                graph[nx][ny] = graph[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    return graph[n-1][m-1];
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%1d", &graph[i][j]);
        }
    }

    cout << bfs(0, 0);
}