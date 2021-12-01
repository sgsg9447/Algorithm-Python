#n과 m시리즈 1번

# from itertools import permutations
# n,m = map(int, input().split())

# arr=[i for i in range(1, n+1)]
# ans = list(permutations (arr,m))


n,m = map(int, input().split())
visit = [False] * n
arr= [0] * m
def dfs(depth):
    if depth == m:
        for i in range(0, len(arr)):
            print(arr[i], end=' ')
        print()
        return
    
    for i in range(n):
        if not visit[i]:
            visit[i] =True
            arr[depth] = i + 1
            dfs(depth+1)
            visit[i] = False

dfs(0)

# n,m = map(int,input().split())
# visit = [False] * n
# arr = [0] * m
# def dfs(depth):
#     if depth == m:
#         print(arr)
#         return
#     for i in range(n):
#         if not visit[i]:
#             visit[i]=True
#             arr[depth] = i + 1
#             dfs(depth+1)
#             visit[i] = False

# dfs(0)

# n, m = map(int, input().split())
# visit = [False]*n
# arr = [0] * m
# def dfs(depth):
#     if depth == m:
#         print(arr)
#         return
#     for i in range(n):
#         if not visit[i]:
#             visit[i]=True
#             arr[depth] = i+1
#             dfs(depth+1) 
#             visit[i] = False
# dfs(0)

# n,m = map(int, input().split())
# visit = [False]*n
# arr = [0]*m
# def dfs(depth):
#     if depth == m:
#         print(arr)
#         return
#     for i in range(n):
#         if not visit[i]:
#             visit[i]= True
#             arr[depth] = i+1
#             dfs(depth+1)
#             visit[i] = False
# dfs(0)
