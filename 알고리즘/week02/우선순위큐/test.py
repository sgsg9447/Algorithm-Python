import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

num = int(input())
list = []
for _ in range(num):
    n = int(input())
    list.append(n)

result = heapsort(list)
print(result)

print(len(list))

for i in range(1):
    First_sum = (list[i] + list[i+1])
    Last_sum = First_sum + list[i+2]

print(Last_sum)

