# 반복문으로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        # 중간점 값 > target => 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점 값 < target => 오른쪽 확인
        else:
            start = mid + 1

    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)