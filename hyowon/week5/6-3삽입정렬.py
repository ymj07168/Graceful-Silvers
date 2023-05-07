# 삽입정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    # 인덱스 i부터 1까지 감소
    for j in range(i, 0, -1):
        # 현재 데이터보다 작은 데이터를 만날 때까지 한칸씩 왼쪽으로 이동
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)