# # 퀵으로 풀어보기
N = int(input())
array = []
for i in range(N):
    array.append(int(input()))
array.sort()

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)

for i in range(len(array)):
    print(array[i])




# def quick_sort(array):
#     #리스트가 하나 이하의 원소만을 담고 있다면, 종료.
#     if len(array) <= 1:
#         return array
#     pivot = array[0]
#     tail = array[1:]

#     left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
#     right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
  
# print(quick_sort(array))