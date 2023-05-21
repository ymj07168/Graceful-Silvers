n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

a_list = []
for m_ in m_list:
    if m_ in n_list:
        a_list.append("yes")
    else:
        a_list.append("no")
print(*a_list)