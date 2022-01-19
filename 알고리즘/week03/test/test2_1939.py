from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = [[] for i in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    s[a].append([b,c]) #양방향그래프니까!
    s[b].append([a,c])

def BFS(mid):
    visited[i1] = 1
    q = deque()
    q.append(i1)
    while q:
        start = q.popleft()
        if start == i2:
            return True
        for nx, nc in s[start]:
            if visited[nx] == 0 and mid <= nc:
                q.append(nx)
                visited[nx] = 1
    return False

i1, i2 = map(int, input().split())
low, high = 1, 1000000000
while low <= high:
    visited = [0 for i in range(n+1)]
    mid = (low + high) // 2
    if BFS(mid):
        low = mid +1
    else:
        high = mid - 1
print(high)