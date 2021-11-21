def DFS(v):
    if v == n+1: #3이면 4가되는거니까 종료지점이니까.
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()

    else:
        ch[v]=1 #부분집합으로 사용한것
        DFS(v+1)
        ch[v]=0 #사용하지않는다
        DFS(v+1)


if __name__=="__main__":
    n = int(input())
    ch=[0]*(n+1) #원소를 사용했냐안했냐 체크변수 0으로 초기화  되는! 1부터 쓸거니까 n+1로 넉넉히
    DFS(1)

