# # memory over
# import sys
# sys.setrecursionlimit(10**6)
# """
#     Moo 게임
#     문제에서 조건 그대로 구현
# """
#
# def s(n):
#     if n == 0:
#         return 'moo'
#     else:
#         return s(n-1) + 'm'+'o'*(n+2) + s(n-1)
#
# # print(s(0))
# # print(s(1))
# # print(s(2))
#
# n = int(sys.stdin.readline())
# print(s(n)[n-1])

import math
import sys

sys.setrecursionlimit(10**6)
def s(n):
    if n == 0:
        return 'moo'

    return  s(n - 1) + 'm'+'o'*(n + 2) + s(n-1)

n = int(sys.stdin.readline())

temp = 3
answer = 0
for i in range(1,n+1):
    if temp < n:
        temp = temp*2 + (i+2) +1
    else:
        answer = i-1
        break

print(s(answer)[n-1])