n, m = map(int, input().split())

#m길이
h_list = list(map(int, input().split()))
h_list.sort(reverse = True)
#print(h_list)
cut = max(h_list)
sum = 0
flag = False
while True:
    for i in range(n):
        cutting = h_list[i] - cut
        if cutting>0:
            h_list[i] = h_list[i] - cutting
        #print(h_list)
        if cutting >0:
            sum += cutting
            if sum ==m:
                print(cut)
                flag = True
                break
    if flag:
        break
    cut -=1
    #print(cut)
