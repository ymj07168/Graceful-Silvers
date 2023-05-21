//
// Created by 김민지 on 2023/05/22.
//
#include "iostream"
#include "vector"
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> money;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        money.push_back(x);
    }

    vector<int> d(m+1, 10001);
    d[0] = 0;
    for (int i = 0; i < n; i++) {
        for (int j = money[i]; j < m+1; j++) {
            if (d[j - money[i]] != 10001)
                d[j] = min(d[j], d[j - money[i]]+1);
        }
    }

    if (d[m] == 10001) cout << -1;
    else cout << d[m];
}