//
// Created by 김민지 on 2023/05/07.
//
#include "iostream"
using namespace std;

int main() {
    int arr[] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

    for (int i = 0; i < 9; i++) {
        int minIdx = i;
        for (int j = i + 1; j < 10; j++) {
            if (arr[minIdx] > arr[j]) minIdx = j;
        }
        swap(arr[minIdx], arr[i]);
    }

    for (int i = 0; i < 10; i++) {
        cout << arr[i] << " ";
    }
}