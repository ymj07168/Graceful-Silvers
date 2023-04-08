# chapter 03 그리디
# 3-1 거스름돈
# 500, 100, 50, 10원 무한히 존재
# 거슬러줘야 하는 돈 N원(항상 10의 배수)일 때
# 거슬러줘야 하는 동전 '최소 개수'구하기

# 문제 해설 : 가장 큰 화폐부터 돈을 거슬러 주는 것

money = int(input("손님 돈 주셈: "))

coin500 = (money // 500)
coin100 = (money - 500 * coin500) // 100
coin50 = (money - 500 * coin500 - 100 * coin100) // 50
coin10 = (money - 500 * coin500 - 100 * coin100 - 50 * coin50) // 10

N = coin500 + coin100 + coin50 + coin10
print("동전 N번: " + str(N))
print("==============================")

# 답안 예시
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
    n %= coin # 큰 동전  빼고 남은 돈
print("답안해설의 답: "+str(count))
