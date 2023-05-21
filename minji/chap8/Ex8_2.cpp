//
// Created by 김민지 on 2023/05/22.
//
#include "iostream"
#include "vector"
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> foods;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        foods.push_back(x);
    }

    int d[100] = {0,};

    d[0] = foods[0];
    d[1] = max(foods[0], foods[1]);
    for (int i = 2; i < n; i++) {
        d[i] = max(d[i - 1], d[i - 2] + foods[i]);
    }

    cout << d[n - 1];
}