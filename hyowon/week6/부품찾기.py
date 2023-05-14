# 부품 찾기
import sys

N = int(input())
part_list = list(map(int, sys.stdin.readline().split()))

M = int(input())
req_list = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 이용하기
part_list.sort()

def binary_search(array, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return "yes"

    return "no"

for p in req_list:
    print(binary_search(part_list, p, 0, len(part_list)-1), end=' ')


