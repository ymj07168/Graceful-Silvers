//
// Created by 김민지 on 2023/05/22.
//
#include "iostream"
using namespace std;

int main() {
    int x;
    cin >> x;

    int d[30001] = {0,};

    for (int i = 2; i < x + 1; i++) {
        d[i] = d[i - 1] + 1;
        if (i % 2 == 0) d[i] = min(d[i], d[i/2]+1);
        if (i % 3 == 0) d[i] = min(d[i], d[i/3]+1);
        if (i % 5 == 0) d[i] = min(d[i], d[i/5]+1);
    }

    cout << d[x];
}