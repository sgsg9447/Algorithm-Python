n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dx=[-1,0,1,0] #12시방향, 3시방향, 6시방향, 9시방향
dy=[0,1,0,-1]
a.insert((0,0)*n) #n개의 0으로 초기화된 리스트를 0번행으로 insert!
a.append([0]*n) #맨 밑에도 0 초기화 추가!
for x in a: #x가 a라는 2차원 리스트의 한 행한행!
    x.insert(0,0)
    x.append(0)

for x in a:
    print(x) #격자판 모양으로 나옴


cnt = 0 #개수 세야하니까!
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): #행 / 열 
            cnt += 1
print(cnt)