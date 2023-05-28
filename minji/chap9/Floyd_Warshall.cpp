//
// Created by 김민지 on 2023/05/28.
//
#include "iostream"
#define INF 1e9

using namespace std;

int n, m;
int graph[501][501];

int main() {
    cin >> n >> m;

    // 최단 거리 테이블 초기화
    for (int i = 0; i < 501; i++) {
        fill(graph[i], graph[i] + 501, INF);
    }

    // 자기 자신 -> 자기 자신 비용 0으로 초기화
    for (int i  = 0; i <= n; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == j) graph[i][j] = 0;
        }
    }

    // 간선 정보 저장
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a][b] = c;
    }

    // 플로이드 워셜 알고리즘 수행
    for (int k = 1; k <= n; k++) {
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]);
            }
        }
    }

    // 결과 출력
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (graph[i][j] == INF) cout << "INFINITY" << " ";
            else cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}