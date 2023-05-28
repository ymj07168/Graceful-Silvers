//
// Created by 김민지 on 2023/05/28.
//
#include "iostream"
#include "vector"
#include "queue"
#define INF 1e9

using namespace std;

int n, m, start;                        // n: 노드 개수, m: 간선 개수, start: 시작 노드
vector<pair<int, int>> graph[100001];   // 그래프 전체 정보 배열
int d[100001];                          // 최단 거리 테이블

void dijkstra(int start) {
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});
    d[start] = 0;

    while (!pq.empty()) {
        int dist = -pq.top().first;     // 현재 노드까지의 비용
        int now = pq.top().second;      // 현재 노드
        pq.pop();

        if (d[now] < dist) continue;
        for (int i = 0; i < graph[now].size(); i++) {
            int cost = dist + graph[now][i].second;
            if (cost < d[graph[now][i].first]) {
                d[graph[now][i].first] = cost;
                pq.push(make_pair(-cost, graph[now][i].first));
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

    fill(d, d + 100001, INF);
    dijkstra(start);

    for (int i = 1; i <= n; i++) {
        if (d[i] == INF) cout << "INFINITY" << endl;
        else cout << d[i] << endl;
    }
}