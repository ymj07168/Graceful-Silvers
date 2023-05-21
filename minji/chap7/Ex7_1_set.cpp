//
// Created by 김민지 on 2023/05/14.
// 이코테 chap7
// [실전문제] 부품 찾기 - 집합
//
#include "iostream"
#include "set"
using namespace std;

int main() {
    int n, m;
    set<int> total;

    cin >> n;
    for(int i = 0; i < n; i++) {
        int x;
        cin >> x;
        total.insert(x);
    }

    cin >> m;
    for(int i = 0; i < m; i++) {
        int x;
        cin >> x;
        if (total.find(x) != total.end()) cout << "yes ";
        else cout << "no ";
    }
}
