//
// Created by 김민지 on 2023/05/14.
// 이코테 chap7
// [실전문제] 부품 찾기 - 계수정렬
//
#include "iostream"
using namespace std;

int arr[1000001];

int main () {
    int n, m;

    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr[x]++;
    }

    cin >> m;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        if (arr[x]) cout << "yes ";
        else cout << "no ";
    }
}