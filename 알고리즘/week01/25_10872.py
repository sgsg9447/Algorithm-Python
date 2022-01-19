# def fac(n):
#     if n >= 1:
#         return n * fac(n-1)
#     if n == 0:
#         return 1

# N = int(input())
# print(f'{fac(N)}')


def fac(n):
    if n > 0:
        return n * fac(n-1)
    else:
        return 1

N = int(input())
print(f'{fac(N)}')
 