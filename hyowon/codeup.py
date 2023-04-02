# 코드업
# Python 기초 100제
import sys

# 6019
# y, m, d = input().split('.')
# print(d, m, y, sep='-')

# 6020
# birth, info = input().split('-')
# print(birth+''+info)

#6033
# n = ord(input())
# print(chr(n+1))

#6044
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b, ".2f"))

#6045
# a, b, c = input().split()
# sum = int(a) + int(b) + int(c)
# avg = format(sum / 3, ".2f")
# print(sum ,avg)

#6057
# a, b = input().split()
# print(int(a) == int(b))

#6060
# a, b = input().split()
# print(int(a) & int(b))

#6072
# n = int(input())
# while n != 0:
#     print(n)
#     n = n-1

#6074
# c = ord(input())
# t = ord('a')
# while t <= c:
#     print(chr(t), end=' ')
#     t += 1

#6077
# sum = 0
# n = int(input())
# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum += i
# print(sum)

#6078
# while True:
#     c = input()
#     print(c)
#     if c == 'q':
#         break

#6079
# n = input()
# s = 0
# t = 1
# while True:
#     s += t
#     if s >= int(n):
#         break
#     t += 1
#
# print(t)

#6080
# n, m = input().split()
# n = int(n)
# m = int(m)
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

#6081
# n = input()
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
# for i in range(1, 16):
#     print('%X'%(list.index(n)+1), '*%X'%i, '=%X'%((list.index(n)+1)*i), sep='')

#6082
# n = int(input())
#
# for i in range(1, n+1):
#     if i // 10 == 3:
#         print("X", end='')
#     if i % 10 != 0 and (i % 10) % 3 == 0:
#         print("X", end=' ')
#     else:
#         print(i, end=' ')

#6083
# r, g, b = input().split()
# for i in range(0, int(r)):
#     for j in range(0, int(g)):
#         for k in range(0, int(b)):
#             print(i, j, k)
# print(int(r)*int(g)*int(b))

#6088
# a, d, n = input().split()
# a = int(a)
# d = int(d)
# n = int(n)
# print(a + (n-1)*d)

#6089
# a, r, n = input().split()
# a = int(a)
# r = int(r)
# n = int(n)
#
# print(a*(r**(n-1)))

#6090
# a, m, d, n = input().split()
# a = int(a)
# m = int(m)
# d = int(d)
# n = int(n)
#
# res = a
# for i in range(2, n+1):
#     res = res * m + d
#
# print(res)

#6091
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
#
# d = 1
# while d%a!=0 or d%b!=0 or d%c!=0 :
#   d += 1
# print(d)

#6094
# n = int(input())
# a = input().split()
# # 10 4 2 3 6 6 입력 시
# # a = ['10', '4', '2', '3', '6', '6']로 저장
#
# for i in range(len(a)):
#     a[i] = int(a[i])
#
# a.sort()
# print(a[0])

#6096
# d = []
#
# for i in range(19):
#     l = input().split()
#     d.append(l)
#
# for i in range(19):
#     for j in range(19):
#         d[i][j] = int(d[i][j])
#
# n = int(input())
#
# for i in range(n):
#     x, y = input().split()
#     for j in range(19):
#         if d[j][int(y)-1] == 0:
#             d[j][int(y)-1] = 1
#         else:
#             d[j][int(y)-1] = 0
#
#         if d[int(x)-1][j] == 0:
#             d[int(x)-1][j] = 1
#         else:
#             d[int(x)-1][j] = 0
#
# for i in range(19):
#     for j in range(19):
#         print(d[i][j], end=' ')
#     print('')

#6097
# import sys
# h, w = map(int, sys.stdin.readline().split())
#
# c = [[0 for j in range(w)] for i in range(h)]
# n = int(input())
# for k in range(n):
#     l, d, x, y = map(int, sys.stdin.readline().split())
#
#     c[x-1][y-1] = 1
#     if d == 0:
#         for r in range(1, l):
#             c[x-1][y-1+r] = 1
#     else:
#         for r in range(1, l):
#             c[x-1+r][y-1] = 1
#
# for i in range(h):
#     for j in range(w):
#         print(c[i][j], end=' ')
#     print('')

#6098
h = []
for i in range(10):
    w = sys.stdin.readline().split()
    h.append(w)

for i in range(10):
    for j in range(10):
        h[i][j] = int(h[i][j])

x = 2
y = 2
h[x-1][y-1] = 9
while True:
    if x-1 > 9 or y-1 > 9:
        break

    if h[x-1][y] != 1:
        y += 1
    elif h[x][y-1] != 1:
        x += 1
    else:
        break

    if h[x-1][y-1] == 2:
        h[x - 1][y - 1] = 9
        break

    h[x-1][y-1] = 9

for i in range(10):
    for j in range(10):
        print(h[i][j], end=' ')
    print('')

