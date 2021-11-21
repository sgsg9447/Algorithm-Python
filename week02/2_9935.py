from collections import deque
string = list(input())
n = len(string)
dq = list(string)
dq =deque(dq) #dq라는 리스트가 deque라는 자료구조가 된것
bomb = input()

while bomb in string:
    for str in string:
        for b in bomb:
            if str == b:
                dq.popleft()
            else:
                move_num = dq.popleft()
                dq.append(move_num)


                if len(dq) != 0:
                    print(dq)
                else:
                    print("FRULA")


# 구조는 먼저, deque자료구조를 이용하여, string의 문자열과, bomb의 문자열이 같을 경우 dq.popleft() 하고, 다를경우 빼고 뒤로 넘겨서 문자열을 맞추려고 생각하였으나.
# for문을 계속돌게되고, print 실행 순서가 원하는대로 되지않아 다시 해보아야함..!