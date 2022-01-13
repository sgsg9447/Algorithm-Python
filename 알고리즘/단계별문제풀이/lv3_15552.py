# #input 값 받을때 sys.stdin.readline()으로 하면 더 빠르게 수행가능!
# import sys
# t=int(sys.stdin.readline())#테스트케이스 갯수
# for i in range(t):
#     a,b = map(int,sys.stdin.readline().split())
#     print(a+b)

import sys

input= sys.stdin.readline

t=int(input())
for i in range(t):
  A,B=input().split()
  print(int(A)+int(B))