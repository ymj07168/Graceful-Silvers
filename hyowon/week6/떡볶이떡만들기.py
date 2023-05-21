# 떡볶이 떡 만들기
import sys

N, M = map(int, sys.stdin.readline().split())
rice_cake = list(map(int, sys.stdin.readline().split()))

def binary_search(rice_cake, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        sum = 0
        for r in rice_cake:
            if r > mid:
                sum += (r-mid)

        if sum > target:
            start = mid + 1
        elif sum < target:
            end = mid - 1
        elif sum == target:
            return mid

    # 모든 떡의 길이가 같거나, 차이가 없는 경우의 문제 처리
    # 가장 긴 떡의 길이부터 감소시켜가며 검사
    max_len = max(rice_cake)
    # 위에서 구한 sum값 초기화
    sum = 0
    while True:
        sum = 0
        for r in rice_cake:
            if r > max_len:
                sum += (r-max_len)

        if sum >= target:
            return max_len
        else:
            max_len -= 1


result = binary_search(rice_cake, M, min(rice_cake), max(rice_cake))
print(result)