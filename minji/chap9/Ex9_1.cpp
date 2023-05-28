//
// Created by 김민지 on 2023/05/29.
// 미래도시 : 플로이드 워셜 문제
//
#include "iostream"
#define INF 1e9

using namespace std;

int n, m;
int graph[101][101];
int x, k;

int main() {
    cin >> n >> m;
    for (int i = 0; i < 101; i++) {
        fill(graph[i], graph[i] + 101, INF);
    }

    for (int i  = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j) graph[i][j] = 0;
        }
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    cin >> x >> k;

    for (int k = 1; k <= n; k++) {
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]);
            }
        }
    }

    int d = graph[1][k] + graph[k][x];
    if (d >= INF) cout << -1;
    else cout << d;
}
