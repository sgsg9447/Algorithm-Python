# n,k= map(int, input().split())
# c=[0]*(k)
# list=[]
# for _ in range(n):
#     weight, price = map(int,input().split())
#     list.append((weight,price))
# for i in range(k):
#     c[i] = int(input())

# sorted_list = sorted(list, key = lambda x : x[1], reverse=True)
# #sorted_list의 값중 앞부터 꺼내서 가방채우기

# for j in range(k):
#     for x,y in sorted_list:
#         if x < c[j]:

import sys
import heapq

input = sys.stdin.readline
n,k = map(int,input().split())

jew = []
for _ in range(n):
    heapq.heappush(jew, list(map(int,input.split())))
bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()

ans = 0
tmp_jew=[]
for bag in bags:
    while jew and bag >= jew [0][0]:
        #최대힙이니까 - 이지 !
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        ans -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(ans)