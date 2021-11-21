import sys

from collections import deque
n, k = map(int, input().split())
dq = list(range(1,n+1))
dq =deque(dq) #dq라는 리스트가 deque라는 자료구조가 된것
new_list = []
while len(dq) != 1:
    for i in range (k-1):
        cur = dq.popleft()
        dq.append(cur)
    plus = dq.popleft()

    new_list.append(plus)
if len(dq) == 1:
    last = dq.popleft()
    new_list.append(last)

print("<" + ", ".join(map(str, new_list)) + ">")
