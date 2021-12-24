#첫번째 시도. list의 append 하니 런타임에러뜸
# import sys

# input = sys.stdin.readline

# n = int(input())
# list = []
# for _ in range(n):
#     a = int(input())
#     list.append(a)

# dp = [0]*(n+1)

# dp[0] = list[0]

# dp[1] = list[0] + list[1]
# dp[2] = max(list[1] + list[2], list[0] + list[2])
# for i in range(3, n):
#     dp[i] = max(dp[i - 3] + list[i - 1] + list[i], dp[i - 2] + list[i])
# print(dp[n-1])

#두번째 시도. list의 길이를 n+1로하니 런타임에러 뜸
# n = int(input())
# list = [0]*(n+1)
# for i in range(n):
#     list[i] = int(input())

# dp = [0]*(n+1)

# dp[0] = list[0]

# dp[1] = list[0] + list[1]
# dp[2] = max(list[1] + list[2], list[0] + list[2])
# for i in range(3, n):
#     dp[i] = max(dp[i - 3] + list[i - 1] + list[i], dp[i - 2] + list[i])
# print(dp[n-1])

#세번째 시도. n을 문제에서 주어진 300개 이하여서 301로 하니 성공
n = int(input())
list = [0]*(301)
for i in range(n):
    list[i] = int(input())

dp = [0]*(301)

dp[0] = list[0]
dp[1] = list[0] + list[1]
dp[2] = max((list[1] + list[2]), (list[0] + list[2]))
for i in range(3, n):
    dp[i] = max((dp[i - 3] + list[i - 1] + list[i]), (dp[i - 2] + list[i]))
print(dp[n-1])

