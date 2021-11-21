import sys
import heapq as hq

max_heap = [] #빈 리스트 만들기!
min_heap = []

num = (int(sys.stdin.readline())) #총 입력받는 개수

for i in range(num):
    n = (int(sys.stdin.readline())) #값을 비교해야하니까!
    if len(max_heap) == len(min_heap):
        hq.heappush(max_heap,-n)
    else: 
        hq.heappush(min_heap,n)
     
    if len(max_heap) >=1 and len(min_heap) >= 1 and max_heap[0] * -1 > min_heap[0]: #-1 곱한이유는 최댓값힙으로 바꿔주려고!
            max_value = hq.heappop(max_heap) * -1
            min_value = hq.heappop(min_heap)

            hq.heappush(max_heap, min_value*-1)
            hq.heappush(min_heap, max_value)

    print(max_heap[0] * -1)
    
    
# 왼쪽힙은 최대힙으로 정렬하고, 오른쪽힙은 최소힙으로 정렬. 
# 최소힙의 - 값곱한것은 최대힙이된다.
