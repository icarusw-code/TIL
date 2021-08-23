#완전 탐색 유형
#python은 1초에 2천만번 안에 수행 되는지 합리적으로 판단 하면 된다.


h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j)+ str(k):
                count += 1
        
print(count)