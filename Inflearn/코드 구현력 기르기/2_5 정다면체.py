# 두눈의 합의 값을 인덱스 번호라고 생각하고, 인덱스 부분을 1 증가!

n,m = map(int,input().split())
cnt = [0] * (n+m+3) #왜 3했지? > 
max = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for i in range(n+m+1):
    if cnt[i]> max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] ==max:
        print(i, end=' ') #옆으로 출력!