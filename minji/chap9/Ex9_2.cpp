//
// Created by 김민지 on 2023/05/29.
// 전보 : 다익스트라 문제
//
#include "iostream"
#include "vector"
#include "queue"
#define INF 1e9

using namespace std;

int n, m, c;
vector<pair<int, int>> graph[30001];
int d[30001];

int dijkstra(int start) {
    priority_queue<pair<int, int>> pq;
    pq.push({0, start});
    d[start] = 0;

    while (!pq.empty()) {
        int dist = -pq.top().first;
        int now = pq.top().second;
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

int main() {
    cin >> n >> m >> c;

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
    }

    fill(d, d + 30001, INF);
    dijkstra(c);

    int sum = 0;
    int max = 0;
    for (int i = 1; i <= n; i++) {
        if (d[i] != INF) {
            sum++;
            if (max < d[i]) max = d[i];
        }
    }

    cout << sum - 1 << " " << max;
}