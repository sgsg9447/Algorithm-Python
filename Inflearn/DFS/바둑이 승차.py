def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum >c:
        return

    if L == n: #부분집합 완성 말단노드다! 
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__=="__main__":
    c,n = map(int, input().split())
    a=[0]*n #바둑이 각각의 무게를 리스트에 저장 
    result = -2147000000 #최종적인 값을 찾는데 가장 작은 값으로 초기화!result = float('-inf')

    for i in range(n):
        a[i]=int(input())
    total = sum(a)
    DFS(0,0,0)
    print(result)

