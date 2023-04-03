# #1
# print("Hello")
#
# #2
# print("Hello World")
#
# #3
# print("Hello")
# print("World")
#
# #4
# print("'Hello'")
#
# #5
# print('"Hello World"')
#
# #6
# print("\"!@#$%^&*()'")
#
# #7
# print("\"C:\Download\\'hello'.py\"")
#
# #8
# print('print("Hello\\nWorld")')
#
# #9
# c = input()
# print(c)
#
# #10
# n = int(input())
# print(n)

# #11
# f = float(input())
# print(f)

# #12
# a = int(input())
# b = int(input())
# print(a)
# print(b)

# #13
# a = input()
# b = input()
# print(b)
# print(a)
#
# #14
# f = float(input())
# print(f)
# print(f)
# print(f)

# #15
# a, b = map(int, input().split())
# print(a)
# print(b)
#
# #16
# c1, c2 = input().split()
# print(c2, c1)

# #17
# s = input()
# print(s, s, s)

# #18
# a, b = input().split(':')
# print(a, b, sep=':')

# #19
# y, m, d = input().split('.')
# print(d + "-" + m + "-" + y)
#
# #20
# c1, c2 = input().split('-')
# print(c1 + c2)

# #21
# s = input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

# #22
# s = input()
# print(s[0:2], s[2:4], s[4:6])

# #23
# a, b, c = input().split(':')
# print(b)

# #24
# w1, w2 = input().split()
# s = w1 + w2
# print(s)

# #25
# a, b = input().split()
# c = int(a) + int(b)
# print(c)

# #26
# a = float(input())
# b = float(input())
# print(a + b)

# #27
# n = int(input())
# print('%x'% n)        #16진수 출력

# #28
# n = int(input())
# print('%X' % n)       #16진수 대문자로 출력

# #29
# a = input()
# n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
# print('%o' % n)     #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

# #30
# n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
# print(n)

# #31
# c = int(input())
# print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다.
#
# #32
# n = int(input())
# print(-n)
#
# #33
# n = ord(input())  #10진수로 받으면 문자도 더할 수 있음.
# print(chr(n+1))
#
# #34
# a, b = map(int, input().split())
# print( a - b)

# #35
# a, b = map(float, input().split())
# print( a * b)

# #36
# w, n = input().split()
# print(w*int(n))

# #37
# a, b = map(int, input().split())
# print(a % b)

# #38
# n = input()
# s = input()
# print(int(n)*s)

# #39
# a, b = map(int, input().split())
# print(a**b)

#40
# a, b = map(float, input().split())
# print(a**b)
#
# #41
# a, b = map(int, input().split())
# print(a // b)

# #42
# a=float(input())
# print( format(a, ".2f") )
#
# # #43
# a, b = map(float, input().split())
# print(format(a/b , ".3f"))

# #44
# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(format(a/b , ".2f"))

# #45
# a, b, c = map(int, input().split())
# d = a + b + c
# e = format( d/3 , ".2f")
# print(d, e)

# #46
# n = int(input())
# print(n<<1)

# #47
# a, b = map(int, input().split())
# print(a << b)

# #48
# a, b = map(int, input().split())
# if a < b:
#     print("True")
# else:
#     print("False")

# #49
# a, b = map(int, input().split())
# if a == b:
#     print("True")
# else:
#     print("False")
#
# #50
# a, b = map(int, input().split())
# if a <= b:
#     print("True")
# elif a != b:
#     print("False")

# #51
# a, b = map(int, input().split())
# if a != b:
#     print("True")
# elif a == b:
#     print("False")

# #52
# n = int(input())
# print(bool(n)) #bool( ) 을 이용하면 입력된 식이나 값을 평가해 불 형의 값(True 또는 False)을 출력

# #53
# a = bool(int(input()))
# print(not a)

# #54
# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))

# #55
# a, b = input().split()
# print(bool(int(a)) or bool(int(b)))
#
# #56
# a, b = input().split()
# c = bool(int(a))
# d = bool(int(b))
# print((c and (not d)) or (d and (not c)))

# #57
# a, b = input().split()
# print((not(bool(int(a))) and not(bool(int(b)))))
#
# #58
# a = int(input())
# print(~a)

# #59
# a, b = map(int, input().split())
# print(a & b)

#61
# a, b = map(int, input().split())
# print(a | b)
#
# #62
# a, b = map(int, input().split())
# print(a ^ b)

# #63
# a, b = map(int, input().split())
# if a >= b:
#     print(a)
# else:
#     print(b)

#64
# a, b, c = map(int, input().split())
# if a < b:
#     n = a
# else:
#     n = b
#
# if n < c:
#     n = n
# else:
#     n = c
#
# print(n)

# #65
# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print(a)
# if b % 2 == 0:
#     print(b)
# if c % 2 == 0:
#     print(c)

# #66
# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
# if b % 2 == 0:
#     print("even")
# else:
#     print("odd")
# if c % 2 == 0:
#
#     print("even")
# else:
#     print("odd")
#
# #67
# a = int(input())
# if a < 0:
#     if a % 2 == 0:
#         print("A")
#     else:
#         print("B")
#
# if a > 0:
#     if a % 2 == 0:
#         print("C")
#     else:
#         print("D")

# #68
# a = int(input())
# if 90 <= a <= 100:
#     print('A')
# if 70 <= a <= 89:
#     print('B')
# if 40 <= a <= 69:
#     print('C')
# if 0 <= a <=39:
#     print('D')
#
# #69
# n = input()
# if n == "A":
#     print("best!!!")
#
# elif n == "B":
#     print("good!!")
# elif n == "C":
#     print("run!")
# elif n == "D":
#     print("slowly~")
# else:
#     print("what?")

# #70
# #12, 1, 2 : winter
# # 3, 4, 5 : spring
# # 6, 7, 8 : summer
# # 9, 10, 11 : fall
# n = int(input())
# if n//3==1 :
#   print("spring")
# if n//3==2:
#     print("summer")
# if n//3==3:
#     print("fall")
# if n//3==0 or n//3==4:
#     print("winter")
#
# #71
# n = 1      #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
# while n!=0 :
#     n = int(input())
#     if n!=0 :
#         print(n)
#     elif n == 0:
#         break

# #72
# n = int(input())
# while n!=0 :
#   print(n)
#   n = n-1
#
# #73
# n = int(input())
# while n!=0 :
#   n = n-1
#   print(n)

# #74
# c = ord(input())
# t = ord('a')
# while t<=c :
#   print(chr(t), end=' ')
#   t += 1

# #75
# n = int(input())
# k = 0
# while k <= n:
#     print(k)
#     k += 1
# #76
# n = int(input())
# for i in range(n+1) :
#     print(i)

# #77
# n = int(input())
# s = 0
# for i in range(1, n+1) :
#   if i%2==0 :
#     s += i
# print(s)
#
##78
# n = input()
# while True:
#     if n!= 'q':
#         print(n)
#         n = input()
#     elif n == 'q':
#         print(n)
#         break

# #79
# n = int(input())
# s = 0
# t = 0
# while s<n :
#   t = t+1
#   s = s+t
#
# print(t)

# #80
# n, m = map(int, input().split())
# for i in range(1, n+1) :
#   for j in range(1, m+1) :
#     print(i, j)
#
# #81
# n = int(input(), 16)
# for i in range(1, 16) :
#   print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
#
# #82
# n = int(input())
# for i in range(1, n+1):
#     if i%10==3 or i%10==6 or i%10==9 :
#         print("X", end=' ')
#     else:
#         print(i, end=' ')
#
# ##83
# r, g, b  = map(int, input().split())
# for i in range(0, r) :
#   for j in range(0, g) :
#       for k in range(0, b):
#         print(i, j, k)
#
# print(r*g*b)

# #84
# a, b, c, d = map(int, input().split())
# print(format(a * b * c * d /8/1024/1024, ".1f")+ " MB")
#
# #85
# a, b, c = map(int, input().split())
# print(format(a * b * c /8/1024/1024, ".2f")+ " MB")

# #86
# n = int(input())
# s = 0
# c = 0
# while True :
#   s += c
#   c += 1
#   if s>=n :
#     break
#
# print(s)

# #87
# n = int(input())
# for i in range(1, n+1):
#   if i%3==0 :
#     continue            #다음 반복 단계로 넘어간다.
#   print(i, end=' ')    #i가 3의 배수가 아닐 때만 실행된다.

# #88
# a, b, c = map(int, input().split())
# for i in range(1, c):
#     a = a + b
#
# print(a)

##89
# a, b, c = map(int, input().split())
# for i in range(1, c):
#     a = a * b
#
# print(a)

# #90
# a, b, c, d= map(int, input().split())
# for i in range(1, d):
#     a = a * b + c
# print(a)

# #91
# a, b, c = map(int, input().split())
# d = 1
# while d%a!=0 or d%b!=0 or d%c!=0 :
#   d += 1
# print(d)

# #92
# n = int(input())      #개수를 입력받아 n에 정수로 저장
# a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장
#
# for i in range(n) :  #0부터 n-1까지...
#   a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장
#
# d = []                     #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
# for i in range(24) :  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
#   d.append(0)        #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.
#
# for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
#   d[a[i]] += 1
#
# for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
#   print(d[i], end=' ')


# #93
# n = int(input())      #개수를 입력받아 n에 정수로 저장
# a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장
#
# for i in range(n) :  #0부터 n-1까지...
#   a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장
#
# d = []                     #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
# for i in range(24) :  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
#   d.append(0)        #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.
#
# for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
#   d[a[i]] += 1
#
# for i in range(n-1, -1, -1) :
#   print(a[i], end=' ')

#
# #94
# n = int(input())
# a = input().split()
#
# for i in range(n) :
#   a[i] = int(a[i])
#
# min = a[0]
# for i in range(0, n) :
#   if a[i] < min :
#     min = a[i]
#
# print(min)

# #95
# d=[]                        #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
# for i in range(20) :
#   d.append([])         #리스트 안에 다른 리스트 추가해 넣기
#   for j in range(20) :
#     d[i].append(0)    #리스트 안에 들어있는 리스트 안에 0 추가해 넣기
#
# n = int(input())
# for i in range(n) :
#   x, y = input().split()
#   d[int(x)][int(y)] = 1
#
# for i in range(1, 20) :
#   for j in range(1, 20) :
#     print(d[i][j], end=' ')    #공백을 두고 한 줄로 출력
#   print()                          #줄 바꿈



#97
h, w = map(int, input().split())
n = int(input())
m = []
for i in range(h+1) :
  m.append([])
  for j in range(w+1) :
    m[i].append(0)

for i in range(n) :
    l, d, x, y = map(int, input().split())
    if int(d) == 0:
        for j in range(int(l)):
            m[int(x)][int(y) + j] = 1
    else:
        for j in range(int(l)):
            m[int(x) + j][int(y)] = 1

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            print(m[i][j], end=' ')
        print()
