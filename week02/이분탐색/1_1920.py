
# def binary(element, some_list, start, end):
#     if end == :
#         end = len(some_list)-1
#     if start > end:
#         return 0

#     mid = (start + end) // 2

#     if element == some_list[mid]:
#         return 1
#     elif element < some_list[mid]:
#         end = mid - 1
#     elif element > some_list[mid]:
#         start = mid + 1
#     return binary(element, some_list, start, end)

# n = int(input())
# n_list = list(map(int, input().split()))
# sorted_list = sorted(n_list)

# m = int(input())
# m_list = list(map(int,input().split()))

# for i in range(len(n_list)):
#     print(binary(m_list[i],sorted_list))


# #------------------------------------------------
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()

# print(a)

# m = int(input())
# m_list = list(map(int,input().split()))

# start = 0
# end = n-1
# while start <= end:
#     mid = (start+end)//2
#     for m in m_list:
#         if a[mid] == m: #a의 중간에 있는 값이 입력받은 m과 같은지?
#             print(1) # 몇번째 이냐니까, +1
#             break
#         elif a[mid]>m:
#             end = mid-1
#         else:
#             start = mid + 1
# else: 
#     print(0)


import sys
while True:
    N = list(map(int,sys.stdin.readline().split()))
    n = N[0]
    if n == 0:
        break
    height = [0] + N[1:] + [0]
    check = [0]
    area = 0
    for i in range(1, n + 2):
        while(check and (height[check[-1]] > height[i])):
            cur_height = check.pop()
            area = max(area, (i-check[-1]-1) * height[cur_height])
        check.append(i)
    print(area)
