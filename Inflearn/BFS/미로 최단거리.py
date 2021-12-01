import sys
from collections import deque

dx = [-1, 0, 1, 0] #12시방향, 3시방향, 6시방향, 9시방향
dy = [0, 1, 0, -1]
board = [list(map(int,input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)] #0으로 초기화 무조건 7,7로 들어온댓으니까!
Q = deque()
Q.append((0,0))
board[0][0]=1 #한번 방문한곳은 1로 벽으로 만들기
while Q: # Q가 비면 거짓이되어서 멈추도록!
    tmp = Q.popleft()
    for i in range(4): #하나가 나오면 무조건 네방향 탐색해야하니까
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0<=y<=6 and board[x][y]==0: #통로여야 가지!
            board[x][y]=1 #벽으로 만드는것
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))
if dis[6][6]==0:
    print(-1)
else: 
    print(dis[6][6])

