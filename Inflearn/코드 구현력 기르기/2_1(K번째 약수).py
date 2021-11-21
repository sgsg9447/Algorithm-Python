# #슬기풀이
# #빈배열을 만들어서, 만약 약수이면 빈배열에 append 해주고 싶음. 

# n, k = map(int, input().split())
# arr = []
# for i in range(1, n+1):
#     if n % i == 0:
#         arr.append(i)
# if len(arr) < k:   
#     print(-1)
# else:
#     print(arr[k-1])

#----------------------------------------
#인프런 풀이

# n, k = map(int, input().split())
# cnt = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else: 
#     print(-1)


