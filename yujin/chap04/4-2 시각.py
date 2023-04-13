N = int(input())
count = 0
for h in range(N+1):
    # 0~23시
    for m in range(60):
        # 0~60분
        for s in range(60):
            # 0~60초
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                #print(h, m, s)
                count+=1

print(count)
