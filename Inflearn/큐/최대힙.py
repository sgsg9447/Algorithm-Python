#최소힙 문제에서 부호만 반대로!

import heapq as hq

a = [] #빈 리스트 만들기!
while True:
    n = int(input()) #값을 비교해야하니까!
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a)) #heappop이라는 함수가 a에서 자료를 하나 팝해주는데 (끄집어내주는데) 루트 노드값을 팝! 팝해서 리턴받는것
    else:
        hq.heappush(a, -n) #a라는 리스트에 n값을 푸시해라! 넣어라!
         