import sys
from collections import deque

max = 10000 #좌표의 멕시멈!
ch = [0]*(max+1) 
dis = [0]*(max+1)
n,m = map(int, input().split()) #n이 출발점 m이 도착점
ch[n] = 1 #n에서 출발하니까 체크거는거고
dis[n] = 0 #n이 출발점이니까 거리는 0
dq = deque()
dq.append(n)
while dq: 
    now=dq.popleft()
    if now == m:
        break
    for next in(now-1, now+1, now+5): #next가 차례차례 세바퀴 돌게됨.
        if 0 < next <= max:
            if ch[next]==0:
                dq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[m])

