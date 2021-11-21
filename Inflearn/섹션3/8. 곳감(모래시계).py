n = int(input())
a =[list(map(int,input().split())) for _ in range(n)] #한줄읽어서 리스트화 시킨것!
m = int(input())
for i in range(m):
    h, t, k =map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
            #h가 2라면 2-1=1 이고 1번째 인덱스 해야 2행이니까! #왼쪽으로 회전하는 효과!
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) #제일 뒤의 값을 0번 인덱스에 넣는다! #오른쪽으로 회전하는 효과!

#모래시계처럼! s = 0 , e = n-1 (n은 5*5행렬이라면, 첫번째줄! 0부터 4까지, 두번째줄은 1부터 3까지 > s는 1증가, e는 1감소 )

res=0
s= 0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)