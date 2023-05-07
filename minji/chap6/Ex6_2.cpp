//
// Created by 김민지 on 2023/05/08.
//
#include "iostream"
#include "vector"
using namespace std;

bool compare(const pair<string, int>& a, const pair<string, int>& b) {
    return a.second < b.second;
}

int main() {
    vector<pair<string, int>> students;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string name;
        int score;
        cin >> name >> score;
        students.push_back(make_pair(name, score));
    }

    sort(students.begin(), students.end(), compare);

    for (int i = 0; i < n; i++) {
        cout << students[i].first << " ";
    }
}