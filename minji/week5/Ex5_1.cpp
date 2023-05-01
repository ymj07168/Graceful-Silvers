//
// Created by 김민지 on 2023/05/01.
//
#include "iostream"

using namespace std;

int n, m;
int graph[1000][1000];

bool dfs(int x, int y) {

    if (x < 0 || x >= n || y < 0 || y >= m) return false;

    if (!graph[x][y]) {
        // 방문 처리
        graph[x][y] = 1;

        // 상하좌우 재귀 호출
        dfs(x-1, y);
        dfs(x+1, y);
        dfs(x, y-1);
        dfs(x, y+1);

        // 1개만 있더라도 true
        return true;
    }
    return false;
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // cin >> graph[i][j];
            scanf("%1d", &graph[i][j]);
        }
    }

    int result = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (dfs(i, j)) result++;
        }
    }

    cout << result;
}
