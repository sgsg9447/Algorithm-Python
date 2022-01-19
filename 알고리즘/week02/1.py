from collections import deque
string = list(input())
dq =deque(string) #dq라는 리스트가 deque라는 자료구조가 된것
stack = []

for i in range(len(string)):
    bomb = list(input())
    for j in range(len(bomb)):
        if str[i] != bomb[i]:
            move_num = dq.popleft()
            dq.append(move_num)
        else:
            cur = stack.pop()
            stack.append(cur)

# if len(dq) != 0:
#         print(dq)
# else:
#     print("FRULA")


# from collections import deque
# n = int(input())
# dq = list(range(1,n+1))
# dq =deque(dq) #dq라는 리스트가 deque라는 자료구조가 된것
# while(not (len(dq) == 1)):
#     dq.popleft()
#     move_num = dq.popleft()
#     dq.append(move_num)


# print(dq[0])
