//
// Created by 김민지 on 2023/05/14.
// 이코테 chap7
// [실전문제] 부품 찾기 - 이진탐색
//
#include "iostream"
#include "vector"
using namespace std;

bool binarySearch(vector<int> &arr, int target, int start, int end) {
    if (start > end) return false;
    int mid = (start + end) / 2;

    if (arr[mid] == target) return true;
    else if (arr[mid] > target) return binarySearch(arr, target, start, mid-1);
    else return binarySearch(arr, target, mid+1, end);
}

int main () {
    int n, m;
    vector<int> total;

    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        total.push_back(x);
    }
    sort(total.begin(), total.end());

    cin >> m;
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        int result = binarySearch(total, x, 0, n-1);
        if (result) cout << "yes ";
        else cout << "no ";
    }
}