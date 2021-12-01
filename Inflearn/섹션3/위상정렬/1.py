#위상정렬: 순서가 정해져있는 작업을 차례로 수행해야할 때 그 순서를 정해주기 위해 사용하는 알고리즘


from collections import deque
#n=노드 m=간선
n,m = map(int, input().split())
#인덱스번호를 맞추기위해 n+1개
graph = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)
dq=deque()

for  i in range(m):
    a,b = map(int, input().split())
    graph[a][b]=1 #a행의 b열로 방향성이 있음을 체크
    # graph[a][b] = graph[b][a] = 1 #방향성없을때!
    degree[b]+=1 #진입차수 증가!


for c in graph:
    print(c)

print(f'degree:',degree)

for i in range(1, n+1):
    if degree[i]==0: #진입차수가 0개일때
        dq.append(i) #인덱스는 노드그자체!
print(dq)

while dq:
    x = dq.popleft()
    print(x, end=' ')
    for i in range(1, n+1): #노드n개
        if graph[x][i]==1:
            degree[i] -=1 #i는 도착점
            if degree[i]==0:
                dq.append(i)
        