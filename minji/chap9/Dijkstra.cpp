//
// Created by 김민지 on 2023/05/28.
//
#include "iostream"
#include "vector"
#define INF 1e9

using namespace std;

int n, m, start;                        // n: 노드 개수, m: 간선 개수, start: 시작 노드
vector<pair<int, int>> graph[100001];   // 그래프 전체 정보 배열
bool visited[100001];                   // 방문 여부 체크 배열
int d[100001];                          // 최단 거리 테이블

int getSmallestNode() {
    int min_value = INF;
    int index = 0;
    for (int i = 1; i <= n; i++) {
        if (d[i] < min_value && !visited[i]) {
            min_value = d[i];
            index = i;
        }
    }
    return index;
}

void dijkstra(int start) {
    d[start] = 0;
    visited[start] = true;
    for (int j = 0; j < graph[start].size(); j++) {
        d[graph[start][j].first] = graph[start][j].second;
    }

    for (int i = 0; i < n - 1; i++) {
        int now = getSmallestNode();
        visited[now] = true;

        for (int j = 0; j < graph[now].size(); j++) {
            int cost = d[now] + graph[now][j].second;
            if (cost < d[graph[now][j].first]) {
                d[graph[now][j].first] = cost;
            }
        }
    }
}

int main(void) {
    cin >> n >> m >> start;

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c}); // a노드 -> b노드의 비용이 c
    }

    fill_n(d, 100001, INF);
    dijkstra(start);

    for (int i = 1; i <= n; i++) {
        if (d[i] == INF) cout << "INFINITY" << endl;
        else cout << d[i] << endl;
    }
}