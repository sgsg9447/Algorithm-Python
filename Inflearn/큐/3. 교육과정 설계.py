from collections import deque

need = input()
n = int(input())
for i in range(n):
    plan = input() #과목을 읽고나서
    dq=deque(need) #dq를 초기화!
    for x in plan:
        if x in dq:
            if x != dq.popleft(): #현재 q에 있는 맨 앞자료와 현재 수업이 필수자료가 앞자료가아니다? 그럼 노!
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
            