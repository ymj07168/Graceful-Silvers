import sys

N, M = map(int, input().split())

students = []
for i in range(M):
    task, a, b = map(int, input().split())
    students.append([task, a, b])

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
parent = [0] * (N+1)

for i in range(1, N + 1):
    parent[i] = i

# 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 같은 팀 여부 확인
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


for task, a, b in students:
    if task == 0:
        union_parent(parent, a, b)
    if task == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
