from collections import deque
n, k = map(int, input().split())
dq = list(range(1,n+1))
dq =deque(dq) #dq라는 리스트가 deque라는 자료구조가 된것
while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft() #break 해도 상관없음
