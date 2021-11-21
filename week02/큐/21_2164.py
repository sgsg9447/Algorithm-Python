from collections import deque
n = int(input())
dq = list(range(1,n+1))
dq =deque(dq) #dq라는 리스트가 deque라는 자료구조가 된것
while(not (len(dq) == 1)):
    dq.popleft()
    move_num = dq.popleft()
    dq.append(move_num)


print(dq[0])


