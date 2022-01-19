# from collections import deque
# #상하좌우
# dx = [-1, 0, 1, 0] #12시방향, 3시방향, 6시방향, 9시방향
# dy = [0, 1, 0, -1]
# #배열 크기 nxn
# #바이러스 1~k번만큼있음
# n,k = map(int,input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# #처음 주어진 시험관 배열
# for x in arr:
#     print(x)

# visited = [[0]*(n) for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if arr[i][j] != 0:
#             visited[i][j]=1

# # print('visited')
# # for a in visited:
# #     print(a)

# dq = deque()
# dq.append((0,0))
# print('dq',dq)

# cnt=0

# while dq:
#     cnt+=1
#     tmp = dq.popleft()
#     for i in range(4):
#         x = tmp[0] + dx[i]
#         y = tmp[1] + dy[i]
#         print(f'x:{x} y:{y}')
#         #여기부터 막힘.....
#         if 0 <= x <= n-1 and 0 <= y <= n-1 and arr[x][y]==0 and arr[x][y]<arr[x+i][y+i]:
#             arr[x][y] = arr[x-i][y-i] #arr[x][y]이전값이랑 같아야지
#             visited[x][y]=1
#             dq.append((x,y))

# for i in arr:
#     print(i)

# s,x,y = map(int,input().split())

# if s == cnt:
#     print(arr[x][y])
# elif arr[x][y] == 0:
#     print(0)

#두번째 시도
#경쟁적 전염
import sys, heapq
from collections import deque

input = sys.stdin.readline

#배열 크기 nxn
#바이러스 1~k번만큼있음
n,k = map(int,input().split())
#처음 주어진 시험관 배열
# for x in arr:
#     print(x)
arr = []
# arr.append([list(map(int, input().split())) for _ in range(n)])
for _ in range(n) :
    arr.append(list(map(int,input().split())))

S,X,Y = map(int, input().split())

def BFS(s,x,y):
    if s == 0:
        if arr[x-1][y-1]:
            return arr[x-1][y-1]
        else:
            return 0

    q = []
    
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                heapq.heappush(q,(arr[i][j],i,j))
    
    time = 0
    while time < s and q:
        newQ = []
        while q:
            w, x, y = heapq.heappop(q)
            if x -1 >= 0 and arr[x-1][y] == 0:
                arr[x-1][y] = w
                heapq.heappush(newQ,(w, x-1, y))
            if x +1 <= n-1 and arr[x+1][y] == 0:
                arr[x+1][y] = w
                heapq.heappush(newQ, (w, x+1, y))
            if y -1>=0 and arr[x][y-1] == 0:
                arr[x][y-1] = w
                heapq.heappush(newQ, (w,x,y-1))
            if y +1 <= n-1 and arr[x][y+1] == 0:
                arr[x][y+1] = w
                heapq.heappush(newQ,(w,x,y+1))
        
        time += 1
        q = newQ


    return arr[X-1][Y-1]


print(BFS(S,X,Y))



