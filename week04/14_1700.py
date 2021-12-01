import sys
input = sys.stdin.readline

n,k = map(int,input().split())
multitap = [0]*n
list=list(map(int,input().split()))
res = 0
swap = 0
num =0
max_I = 0

for i in list:
    if i in multitap: #멀티탭안에 i가 있으면 패스
        pass
    elif 0 in multitap: #멀티탭 자리가 비어있으면
        multitap[multitap.index(0)] = i #멀티탭의 리스트 중 0이있는 인덱스를 찾아서 거기에 i를 넣어줘라
    else:
        for j in multitap:
            if j not in list[num:]: #j는 현재 멀티탭에 꼽혀있는 애, 그러면서 앞으로 사용할 일이 없는 애
                swap = j
                break #멀티탭 요소들 하나씩 list에 (앞으로 사용해야할 제품) 없으면 swqp 변수에 j(해당제품)저장 후 break
            elif list[num:].index(j) > max_I: #멀티탭 요소가 list에 존재한다면 앞으로 사용할 예정
                max_I = list[num:].index(j) #언제 사용하는지 index값 구하기
                swap = j
        multitap[multitap.index(swap)] = i #for문 종료 후 멀티탭리스트에서 swap값의 인덱스를 구해 새로 들어갈 전기용품 값으로 바꿔줌
        max_I = swap = 0 #다음 루프에서 사용하기 위해 값 초기화
        res += 1 #전기용품 변경했으므로 카운트 +1
    num += 1
print(res)