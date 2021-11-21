n = int(input())
a =[list(map(int,input().split())) for _ in range(n)] #한줄읽어서 리스트화 시킨것!
res=0
s = e = n // 2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2 :
        s -= 1 #스타트포인트는 하나 작아지고
        e += 1 #엔드포인트는 하나 커지고
    else: #예를들어 5*5행렬에서 i가 3일때 5//2 인 2보다 큰 3이니까 스타트포인트는 0에서 다시 1이 되어야하니까+1 엔드포인트는 -1
        s+=1
        e-=1

print(res)