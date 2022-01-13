n,x = map(int,input().split())
A_list = list(map(int,input().split()))
for i in range(n):
    if A_list[i] < x:
        print(A_list[i], end = ' ')    