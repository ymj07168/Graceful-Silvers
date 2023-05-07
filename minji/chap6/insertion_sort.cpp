//
// Created by 김민지 on 2023/05/07.
//
#include "iostream"
using namespace std;

int main() {
    int arr[] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

    for (int i = 1; i < 10; i++) {
        for (int j = i; j > 0; j--) {
            if (arr[j] < arr[j-1]) swap(arr[j], arr[j-1]);
            else break;
        }
    }

    for(int i = 0; i < 10; i++) {
        cout << arr[i] << ' ';
    }
}