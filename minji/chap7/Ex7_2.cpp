//
// Created by 김민지 on 2023/05/14.
// 이코테 chap7
// [실전문제] 떡볶이 떡 만들기 - 파라메트릭 서치
// 파라메트릭 서치 유형: 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에서 사용, 반복문 구현이 간결함
//
#include "iostream"
#include "vector"
using namespace std;

int main() {
    int n, m;
    vector<int> riceCakes;

    cin >> n >> m;
    int start = 0;
    int end = 0;
    for (int i = 0; i < n; i++) {
        int x = 0;
        cin >> x;
        riceCakes.push_back(x);
        if (x > end) end = x;
    }

    int result = 0;
    while (start <= end) {
        int mid = (start + end) / 2;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int r = riceCakes[i] - mid;
            if (r > 0) sum += r;
        }

        if (sum < m) end = mid - 1;     // 부족하면 더 자르기
        else {
            result = mid;
            start = mid + 1;            // 많으면 덜 자르기
        }
    }

    cout << result;
}