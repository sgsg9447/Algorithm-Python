import sys

def DFS(L, sum):
    if sum>total//2:
        return
    if L == n: #0번 인덱스부터 시작했으니까, L = n=input값인 6이라면, 종료!
        if sum ==(total -sum):
            print("YES")
            sys.exit(0) #함수 종료가 아니라 프로그램 전체종료!
    else:
        DFS(L+1, sum+a[L]) #레벨은 1씩 증가, sum값에 a리스트에L이 가리키고있는 값 부분집합의 원소로 사용하니 더해주기!
        DFS(L+1, sum) 

if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    total = sum(a)
    DFS(0,0) 
    print("NO")

