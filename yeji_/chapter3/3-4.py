n, k = map(int, input().split())
count = 0
while n >=k:
    while n % k != 0:  #n이 k로 나누어떨어지지 않는다면
        n -=1
        count +=1
    n //= k
    count +=1

while n>1:
    n -= 1
    count +=1

print(count)