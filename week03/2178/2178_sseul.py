import sys
from collections import deque
#상하좌우
dx = [-1, 0, 1, 0] #12시방향, 3시방향, 6시방향, 9시방향
dy = [0, 1, 0, -1]
#배열의크기 n*m
n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
visited = [[0]*(m) for _ in range(1)] #0으로 초기화 무조건 n,m로 들어온댓으니까!
q = deque()
q.append((1,1))
visited[1][1]=1 #한번 방문한곳은 1로 벽으로 만들기

# for x in visited:
#     print(x) #격자판 모양으로 나옴

while q: # Q가 비면 거짓이되어서 멈추도록!
    tmp = q.popleft()
    for i in range(4): #하나가 나오면 무조건 네방향 탐색해야하니까
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if  1 <= x <= n   and  1<= y <=m and maze[x-1][y-1]==1: #통로여야 가지!
            visited[x][y]=1 #벽으로 만드는것
            maze[x-1][y-1] = maze[x-1][y-1]+maze[tmp[0]-1][tmp[1]-1]
            q.append((x,y))
for i in maze:
    print(i)

print(maze[n-1][m-1])