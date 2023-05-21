//
// Created by 김민지 on 2023/05/21.
//
#include "iostream"

int d[100];

// top down
int fibo(int x) {
    if (x == 1 || x == 2) return 1;
    if (d[x] != 0) return d[x];
    d[x] = fibo(x - 1) + fibo(x - 2);
    return d[x];
}

// bottom up
int fibo_bu(int x) {
    d[1] = 1;
    d[2] = 2;

    for (int i = 0; i < x + 1; i++) {
        d[i] = d[i-1] + d[i-2];
    }
    return d[x];
}
