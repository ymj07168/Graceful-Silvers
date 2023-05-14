//
// Created by 김민지 on 2023/05/08.
//
#include "iostream"
#include "vector"
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> A, B;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        A.push_back(x);
    }

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        B.push_back(x);
    }

    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    int end = B.size()-1;
    for (int i = 0; i < k; i++) {
        if (A[i] < B[end-i]) swap(A[i], B[end-i]);
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += A[i];
    }
    cout << sum;
}