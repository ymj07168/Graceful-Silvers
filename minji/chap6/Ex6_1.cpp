//
// Created by 김민지 on 2023/05/08.
//
#include "iostream"
#include "vector"
using namespace std;

bool compare(int a, int b) {
    return a > b;
}

int main() {
    vector<int> arr;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr.push_back(x);
    }

    sort(arr.begin(), arr.end(), compare);

    for(int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }

}