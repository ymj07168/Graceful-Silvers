# 코드업
# Python 기초 100제

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
r, g, b = input().split()
for i in range(0, int(r)):
    for j in range(0, int(g)):
        for k in range(0, int(b)):
            print(i, j, k)
print(int(r)*int(g)*int(b))







