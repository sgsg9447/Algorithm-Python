#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제


# for i in range (1,101):
#     print('*'*{i})

# n = int(input())
# w = int(input())

# for i in range(n):
#     print('*', end=' ')
#     if i % w == w - 1:
#         print()

# if n % w:
#     print()

n = int(input())

for i in range(1, n+1):
    print('*'*i)
