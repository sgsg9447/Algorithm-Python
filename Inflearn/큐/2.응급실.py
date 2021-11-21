from collections import deque
n, m = map(int, input().split())
Q = [(idx,val) for idx, val in enumerate(list(map(int,input().split())))]  #[(0,60) , (1, 70)~~]

print(Q)

Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft() #뒤쪽의 대기목록 중에 위험도가 자기보다 높으면, 진료받지않고 Q의 뒤쪽으로 들어가야함
    if any(cur[1]<x[1] for x in Q): #자기보다 위험도가 더 높은사람이있는지 Q의 뒤쪽을 다 봐야함. #(0,60)이라는 튜플값이니까. cur[1]=60 < x[1] Q안의 x값 다 돎
        Q.append(cur) #any면 단 한개라도 참이면 참!
    else:
        cnt += 1
        if cur[0] == m:
            break

print(cnt)     
