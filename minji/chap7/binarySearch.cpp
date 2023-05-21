//
// Created by 김민지 on 2023/05/14.
//
#include "iostream"
#include "vector"
using namespace std;

int binarySearch(vector<int> &arr, int target, int start, int end) {
    if (start > end) return -1;
    int mid = (start + end) / 2;

    if (arr[mid] == target) return mid;
    else if (arr[mid] > target) return binarySearch(arr, target, start, mid-1);
    else return binarySearch(arr, target, mid+1, end);
}

int n, target;
vector<int> arr;

int main() {
    cin >> n >> target;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr.push_back(x);
    }

    int result = binarySearch(arr, target, 0, n-1);
    if (result == -1) cout << "Not Found";
    else cout << result;
}