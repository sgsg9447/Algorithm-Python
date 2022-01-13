#별 오른쪽 정렬!

# n = int(input())

# for i in range(1,n+1):
#     star = '*' * (i)
#     print(star.rjust(n))


N=int(input())
for i in range(1,N+1):
    print(' '*(N-i)+'*'*i)