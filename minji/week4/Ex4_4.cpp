//
// Created by 김민지 on 2023/04/30.
//
#include "iostream"
#include "vector"

using namespace std;

int solution(int n, int m, int a, int b, int d, vector<vector<int>> map) {
    int result = 0;

    // initial state
    map[a][b] = 2;
    result++;

    int dir[4] = {3, 2, 1, 0};
    while (true) {
        int aa, bb, dd = d;
        for (int i = 0; i < 4; i++) {
            switch (dd) {
                case 0: aa = a; bb = b - 1; break;     // N -> check W
                case 1: aa = a - 1; bb = b; break;     // E -> check N
                case 2: aa = a; bb = b + 1; break;     // S -> check E
                case 3: aa = a + 1; bb = b; break;     // W -> check S
            }
            if (!map[aa][bb]) {
                a = aa; b = bb; d = dir[(3-dd+1)%4];
                map[a][b] = 2;
                result++;
                break;
            }
            else dd = dir[(3-dd+1)%4];
        }
        if (dd == d) {
            int aa = a, bb = b;
            switch (d) {
                case 0: aa++; break;     // N -> check W
                case 1: bb--; break;     // E -> check N
                case 2: aa--; break;     // S -> check E
                case 3: bb++; break;     // W -> check S
            }
            if (map[aa][bb] == 1) break;
            else a = aa; b = bb;
        }
    }

    return result;
}

int main() {
    int n, m, a, b, d;
    cin >> n >> m >> a >> b >> d;

    vector<vector<int>> map(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
        }
    }

    cout << solution(n, m, a, b, d, map);
}